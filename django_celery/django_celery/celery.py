import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-celery.settings')
app = Celery('django-celery')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()