import logging
from pyramid_celery import celery_app as app


logger = logging.getLogger()


@app.task(bind=True, name="sum_numbers", queue="tasks.add")
def add(self, x, y):
    
    total = x + y
    
    logger.info("The sum of {} + {} is: {}".format(x, y, total))
    return x + y
