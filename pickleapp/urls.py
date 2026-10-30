from django.urls import path
from . import views

urlpatterns = [
    # FIX: Ensure there is no space before 'predict-penguin/'
path('penguin/', views.predict_penguin_species, name='predict_penguin'),
]
