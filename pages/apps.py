from django.apps import AppConfig
from django.test import  SimpleTestCase


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'


