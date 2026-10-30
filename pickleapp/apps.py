import os
import pickle
from django.apps import AppConfig
from django.conf import settings

class PickleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pickleapp'
    
    model = None 

    def ready(self):
        # 1. Print out the target path to your terminal for verification
        print(f"\n[DEBUG] Django is looking for your model file here:\n{settings.PENGUIN_MODEL_PATH}\n")
        
        if hasattr(settings, 'PENGUIN_MODEL_PATH') and os.path.exists(settings.PENGUIN_MODEL_PATH):
            with open(settings.PENGUIN_MODEL_PATH, 'rb') as file:
                PickleappConfig.model = pickle.load(file)
            print("--- Pickle model loaded successfully into Django Memory! ---\n")
        else:
            # 2. Print a warning if the path check failed
            print("--- WARNING: Model file not found at the above path! ---\n")
