from django.apps import AppConfig


class PcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PC'

    def ready(self):
        import PC.signals