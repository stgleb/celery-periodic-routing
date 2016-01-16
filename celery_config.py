from datetime import timedelta

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True


CELERYBEAT_SCHEDULE = {
    'first_task_every_second': {
        'task': 'tasks.first_task',
        'schedule': timedelta(seconds=1),
        'options': {'queue': 'first'}
    },
    'second_task_every_second': {
        'task': 'tasks.second_task',
        'schedule': timedelta(seconds=1),
        'options': {'queue': 'second'}
    },
    'third_task_every_second': {
        'task': 'tasks.third_task',
        'schedule': timedelta(seconds=1)
    },
}
