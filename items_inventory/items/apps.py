"""
Apps.py
"""
from django.apps import AppConfig


class ItemsConfig(AppConfig):
    """Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'items'
