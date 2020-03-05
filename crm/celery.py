from __future__ import absolute_import, unicode_literals

import os
import sentry_sdk

from celery import Celery
# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.dev_settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.server_settings')

import configurations
configurations.setup()

app = Celery('crm')
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
