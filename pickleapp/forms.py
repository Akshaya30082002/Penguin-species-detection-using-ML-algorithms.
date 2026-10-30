from django import forms

class PenguinPredictionForm(forms.Form):
    culmen_length = forms.FloatField(label="Culmen Length (mm)", min_value=0.0, initial=45.0)
    culmen_depth = forms.FloatField(label="Culmen Depth (mm)", min_value=0.0, initial=18.5)
    flipper_length = forms.FloatField(label="Flipper Length (mm)", min_value=0.0, initial=200.0)
    body_mass = forms.FloatField(label="Body Mass (g)", min_value=0.0, initial=4100.0)
