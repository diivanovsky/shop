from celery import shared_task
import time


@shared_task
def some_task():
    time.sleep(5)
    return 'bimbim bam bam'


@shared_task
def some_task_scheduled():
    return 'bim bim bam bam'
