# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:config.py
@Ide:PyCharm
@Time:2018/8/22 11:11
@Remark:
"""


class CeleryConfig(object):
    broker_url = 'redis://192.168.108.193:6379/0'
    timezone = 'Asia/Shanghai'
    # result_backend = 'redis://127.0.0.1:6379/1'
    enable_utc = False
    result_backend = 'django-db'
    result_expires = 60 * 60 * 24 * 90
    result_serializer = 'json'
    result_persistent = True
    accept_content = ['json']
    task_track_started = True
    imports = ['celeryConfig.tasks']
    beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'
