# Penguin-species-detection-using-ML-algorithms.

  A Multi-Class Machine Learning Classification Project that predicts the species of penguins (Adelie, Chinstrap, or Gentoo) based on their physical traits and geographical location. This project utilizes the modern Palmer Penguins dataset to evaluate and compare the performance of various classification algorithms.

  
📊 Dataset Overview

The dataset consists of structural data collected from 344 penguins across three islands in the Palmer Archipelago, Antarctica.

Target Classes (Species)

• Adelie

• Chinstrap

• Gentoo

Features Evaluated

• Island: Torgersen, Biscoe, or Dream

• Bill Length (mm): Length of the penguin's beak

• Bill Depth (mm): Height of the penguin's beak

• Flipper Length (mm): Length of the penguin's wings

• Body Mass (g): Total weight of the penguin

• Sex: Male or Female.



🛠️ Tech Stack & Libraries

• Language: Python

• Data Processing: Pandas, NumPy

• Visualization: Matplotlib, Seaborn

• Machine Learning: Scikit-Learn, XGBoost



⚙️ Project Pipeline


1. Data Cleaning & Preprocessing

• Handled missing value (NaN) entries via imputation or removal.

• Encoded categorical attributes (island and sex) using One-Hot Encoding / Label Encoding.

• Normalized numerical variables using StandardScaler to optimize model convergence.

2. Exploratory Data Analysis (EDA)

• Plotted feature distributions and correlation matrices.

• Identified flipper length and bill depth as the strongest indicators for differentiating species.

3. Model Training & Evaluation

We trained and evaluated the following classification algorithms:

• Logistic Regression (Baseline model)

• K-Nearest Neighbors (KNN)

• Decision Tree Classifier

• Random Forest Classifier

• XGBoost Classifier


