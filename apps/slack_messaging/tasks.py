from __future__ import (
    absolute_import,
    unicode_literals,
)
from celery import shared_task

@shared_task
def sendMenu(channel=None, menu=None):
    message = 'Menu: Atun con zapallo.' 
    return message