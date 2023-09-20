from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

def validateUnique(model_name, field_name, value):
    try:
        # Get the model dynamically using the provided model_name
        model = apps.get_model(model_name)
        
        # Query the database to check for uniqueness
        exists = model.objects.filter(**{field_name: value}).exists()
        
        return not exists  # Return True if the value is unique
    except LookupError:
        raise ValueError("Model not found: " + model_name)
    except IntegrityError:
        raise ValueError("Field not found: " + field_name)