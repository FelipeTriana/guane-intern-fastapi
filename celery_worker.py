import os
import time

from celery import Celery 
from dotenv import load_dotenv
from celery.utils.log import get_task_logger


# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="create_task")
def create_task():
    time.sleep(1)
    celery_log.info(f"Celery task completed!")
    return 'OK'
   

