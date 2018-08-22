# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:app.py
@Ide:PyCharm
@Time:2018/8/22 10:27
@Remark:实例化celery
"""

import os
from celery import Celery
import django
from .config import CeleryConfig


__all__ = ['app']

class Mycelery(Celery):
    def now(self):
        from datetime import datetime
        return datetime.now(self.timezone)

os.environ.setdefault('DJANFGO_SETTINGS_MODULE','watchmen.settings')
django.setup()
app = Mycelery('data_watchmen')
app.config_from_object(CeleryConfig)
app.autodiscover_tasks()
