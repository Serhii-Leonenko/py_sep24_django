from django.apps import AppConfig


class MessangerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "messanger"

    def ready(self):
        import messanger.signals # noqa
