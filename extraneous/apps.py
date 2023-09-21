from django.apps import AppConfig


class ExtraneousConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extraneous'
