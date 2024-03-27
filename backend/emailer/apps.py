from django.apps import AppConfig


class EmailerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emailer"

    # def ready(self):
    #

    def ready(self) -> None:
        pass
