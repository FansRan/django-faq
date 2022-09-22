"""
Django application configuration
"""

from django.apps import AppConfig


class FaqAppConfig(AppConfig):
    """Django FAQ Application definition"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "faq_app"
    verbose_name = "FAQ Application"
