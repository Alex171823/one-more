 
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.local_settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # noqa: T001


app.conf.beat_schedule = {
    "parsing": {"task": 'celery_app.tasks.parse_quotes',
                "schedule": crontab(minute=0, hour='1,3,5,7,9,11,13,15,17,19,21,23'),
                'args': (['https://quotes.toscrape.com'], 0)}
}
