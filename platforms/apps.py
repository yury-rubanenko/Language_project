from django.apps import AppConfig


# flake8: noqa
class PlatformsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "platforms"

    def ready(self):
        import platforms.signals
