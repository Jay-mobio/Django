from django.apps import AppConfig


class Crm1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm1'
    def ready(self):
        import crm1.signals