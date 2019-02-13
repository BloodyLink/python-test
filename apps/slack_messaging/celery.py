from __future__ import absolute_import, unicode_literals

import os, sys

from celery import Celery
from celery.schedules import crontab

# from .tasks import sendMenu

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('celery_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.timezone = 'America/Santiago'

@app.on_after_configure.connect
def setup_periodic_slack_message(sender, **kwargs):
    app.conf.beat_schedule = {
        'send-menu-every-morning': {
            'task': 'apps.slack_messaging.tasks.sendMenu',
            'schedule': crontab(hour=12, minute=0),
            # 'schedule': 15.0,
    },
}

# @app.task
# def slack_message_sender():
#     return sendMenu()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))