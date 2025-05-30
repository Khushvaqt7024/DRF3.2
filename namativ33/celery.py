import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'namativ33.settings')
app = Celery('namativ33')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
