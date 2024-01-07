from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'