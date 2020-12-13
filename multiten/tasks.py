import logging
from celery import shared_task

logger = logging.getLogger('error')


@shared_task
def error_logger(err, exc_info=None):
    if exc_info:
        exc_type, exc_obj, exc_tb = exc_info
        logger.error(f'{exc_tb.tb_frame.f_code.co_filename} {exc_tb.tb_lineno} {str(err)}')
    else:
        logger.error(f'{str(err)}')
