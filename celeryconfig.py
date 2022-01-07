import transaction

from kombu import Queue, Exchange
from celery.signals import task_success, task_failure, task_retry


## Broker settings
broker_url = "redis://127.0.0.1:6379/0"

imports = [
    "financial_system.tasks.web_crawler"
]


_queue_names = [
    "web_crawler"
]

task_queues = [
    Queue(name, Exchange(name), routing_key=name)
    for name in _queue_names
]


@task_success.connect
def task_sucess_pyramid(*args, **kwargs):
    task = kwargs["sender"]
    if not task.request.is_eager:
        transaction.commit()


@task_retry.connect
@task_failure.connect
def task_failure_pyramid(*args, **kwargs):
    task = kwargs['sender']
    if not task.request.is_eager:
        transaction.abort()
