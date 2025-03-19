import os
from celery import Celery


# Set Django settings as default
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoflix.settings')


# Create Celery-App
app = Celery('videoflix')


# Import configuration from Django settings (CELERY_ prefix)
app.config_from_object('django.conf:settings', namespace='CELERY')


# Automatic task discovery in installed apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')