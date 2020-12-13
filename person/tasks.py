from __future__ import absolute_import, unicode_literals
import sys
from datetime import datetime, date, timedelta, timezone
from celery import shared_task

from .models import Tempoo


@shared_task
def async_temp(tem):
    Tempoo.objects.create(name=str(datetime.now()))
    return True
