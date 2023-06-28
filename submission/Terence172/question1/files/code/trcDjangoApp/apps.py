from django.apps import AppConfig


class TrcdjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trcDjangoApp'

    def ready(self):
            import trcDjangoApp.signals

    