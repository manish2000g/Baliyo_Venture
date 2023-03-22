from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Services'

    def ready(self):
        import Services.signals
