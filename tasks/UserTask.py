from celery.task import task


@task
def add():
    return 1+2