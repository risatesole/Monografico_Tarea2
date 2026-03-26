from django.apps import AppConfig
from pathlib import Path

class config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "components.core.button"
    path = str(Path(__file__).resolve().parent)
