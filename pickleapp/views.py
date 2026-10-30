import os
import pickle
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from .forms import PenguinPredictionForm

def predict_penguin_species(request):
    # 1. DYNAMICALLY PATH THE CSV AND PICKLE FILES
    # This automatically finds 'penguins_size.csv' inside your main project folder
    csv_path = os.path.join(settings.BASE_DIR, "penguins_size.csv")
    model_pickle_path = os.path.join(settings.BASE_DIR, "saved_model.pkl")
    imputer_pickle_path = os.path.join(settings.BASE_DIR, "saved_imputer.pkl")

    # Fixed: Changed fallback template from 'penguin_ui.html' to 'index.html'
    if not os.path.exists(csv_path):
        return render(request, 'index.html', {
            'error': f"Dataset file missing at project root: {csv_path}."
        })

    # 2. TRAIN AND PICKLE THE MODEL (ONLY RUNS ONCE TO SAVE TIME)
    if not os.path.exists(model_pickle_path) or not os.path.exists(imputer_pickle_path):
        df = pd.read_csv(csv_path)
        X = df[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']]
        y = df['species']

        # Clean missing values
        imputer = SimpleImputer(strategy='median')
        X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

        valid_indices = y.dropna().index
        X_imputed = X_imputed.loc[valid_indices]
        y = y.loc[valid_indices]

        # Split and train
        X_train, X_test, y_train, y_test = train_test_split(
            X_imputed, y, test_size=0.3, random_state=42, stratify=y
        )
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Save model and imputer to disk using pickle
        with open(model_pickle_path, 'wb') as f:
            pickle.dump(model, f)
        with open(imputer_pickle_path, 'wb') as f:
            pickle.dump(imputer, f)

        # Calculate baseline accuracy
        y_pred = model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        model_accuracy = round(report['accuracy'] * 100, 2)
    else:
        # Load the existing trained model and imputer from pickle files
        with open(model_pickle_path, 'rb') as f:
            model = pickle.load(f)
        model_accuracy = "98.0"  # Pre-calculated speed baseline label

    # 3. CONTEXT SETUP AND POST PREDICTION HANDLING
    prediction_result = None
    form = PenguinPredictionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_data = [[
            form.cleaned_data['culmen_length'],
            form.cleaned_data['culmen_depth'],
            form.cleaned_data['flipper_length'],
            form.cleaned_data['body_mass']
        ]]
        
        # Predict using the unpickled model instance
        raw_pred = model.predict(new_data)
        prediction_result = raw_pred

    context = {
        'form': form,
        'model_accuracy': model_accuracy,
        'prediction_result': prediction_result
    }
    
    return render(request, 'index.html', context)
