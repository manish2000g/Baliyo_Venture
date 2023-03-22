from django.apps import AppConfig


class HeroSectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hero_Section'

    def ready(self):
        import Hero_Section.signals
