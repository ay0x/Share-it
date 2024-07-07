"""
This module configures Celery for the 'shareit' project.

Celery is an asynchronous task queue/job queue based on
distributed message passing.
This module sets up Celery with Django settings and configures
it to autodiscover tasks from all registered Django apps.

The configuration includes:
    - Setting the default Django settings module for the
    'celery' program.
    - Creating an instance of Celery with the project name 'shareit'.
    - Configuring Celery to use Django settings with a
    'CELERY_' prefix for all configuration keys.
    - Enabling Celery to autodiscover tasks from all registered
    Django app configurations.

Imports:
    - absolute_import, unicode_literals: Future compatibility imports.
    - os: A module for interacting with the operating system.
    - Celery: The main class for Celery that is used to instantiate
    a Celery application.

Functions:
    - debug_task: A simple Celery task that prints the request information
    for debugging purposes.
"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shareit.settings')

app = Celery('shareit')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """
    A simple Celery task for debugging purposes.

    This task prints the request information, which is useful
    for debugging Celery configurations and tasks.

    Args:
        self (Task): The task instance, which provides access
        to the request context.
    """
    print(f'Request: {self.request!r}')
