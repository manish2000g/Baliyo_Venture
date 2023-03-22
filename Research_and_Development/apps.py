from django.apps import AppConfig


class ResearchAndDevelopmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Research_and_Development'

    def ready(self):
        import Research_and_Development.signals