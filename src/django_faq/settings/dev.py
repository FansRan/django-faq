"""
Settings for development environment only.

It override the base settings
"""

from django_faq.settings.base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
