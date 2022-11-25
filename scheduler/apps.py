import os

from django.apps import AppConfig
from . import updater


class SchedulerConfig(AppConfig):
    name = 'scheduler'
    
    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            updater.start()
            print("here1")