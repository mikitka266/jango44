from django import AppConfig


class MyprojectConfig(AppConfig):
    default_auto_field= 'django.db.models.BigAutoField'
    name = 'myproject'
    verbose_name = 'Shop'

