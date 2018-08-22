# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:celeryBaseUtils.py
@Ide:PyCharm
@Time:2018/8/22 10:34
@Remark:封装的celery基本操作
"""

import json
from django.core import serializers
from django_celery_beat.models import IntervalSchedule, CrontabSchedule, \
    PeriodicTask
from django_celery_results.models import TaskResult



def get_or_create_interval(interval_type='SECONDS', interval=10):
    if interval_type == 'SECONDS':
        schedule = IntervalSchedule.objects.get_or_create(every=interval,
                                                          period=IntervalSchedule.SECONDS)
    elif interval_type == 'DAYS':
        schedule = IntervalSchedule.objects.get_or_create(every=interval,
                                                          period=IntervalSchedule.DAYS)
    elif interval_type == 'HOURS':
        schedule = IntervalSchedule.objects.get_or_create(every=interval,
                                                          period=IntervalSchedule.HOURS)
    elif interval_type == 'MINUTES':
        schedule = IntervalSchedule.objects.get_or_create(every=interval,
                                                          period=IntervalSchedule.MINUTES)
    elif interval_type == 'MICROSECONDS':
        schedule = IntervalSchedule.objects.get_or_create(every=interval,
                                                          period=IntervalSchedule.MICROSECONDS)
    else:
        raise Exception('interval type error')
    return schedule


def get_or_create_crontab(crontab):
    crontab = crontab.strip()
    crontabs = crontab.split()
    schedule = CrontabSchedule.objects.get_or_create(minute=crontabs[0],
                                                     hour=crontabs[1],
                                                     day_of_week=crontabs[2],
                                                     day_of_month=crontabs[3],
                                                     month_of_year=crontabs[4])
    return schedule


def create_task(schedule, name, task, *args, **kwargs):
    try:
        if isinstance(schedule[0], IntervalSchedule):
            if args and kwargs:
                PeriodicTask.objects.create(
                    interval=schedule[0],
                    name=name,
                    task=task,
                    args=json.dumps(args),
                    kwargs=json.dumps(kwargs)
                )
            elif args:
                PeriodicTask.objects.create(
                    interval=schedule[0],
                    name=name,
                    task=task,
                    args=json.dumps(args),
                )
            elif kwargs:
                PeriodicTask.objects.create(
                    interval=schedule[0],
                    name=name,
                    task=task,
                    kwargs=json.dumps(kwargs)
                )
            else:
                PeriodicTask.objects.create(
                    interval=schedule[0],
                    name=name,
                    task=task,
                )
        elif isinstance(schedule[0], CrontabSchedule):
            if args and kwargs:
                PeriodicTask.objects.create(
                    interval=schedule[0],
                    name=name,
                    task=task,
                    args=json.dumps(args),
                    kwargs=json.dumps(kwargs)
                )
        elif args:
            PeriodicTask.objects.create(
                interval=schedule[0],
                name=name,
                task=task,
                args=json.dumps(args),
            )
        elif kwargs:
            PeriodicTask.objects.create(
                interval=schedule[0],
                name=name,
                task=task,
                kwargs=json.dumps(kwargs)
            )
        else:
            PeriodicTask.objects.create(
                interval=schedule[0],
                name=name,
                task=task,
            )
    except Exception as e:
        return (False, e)
    return (True, None)


def query_result(task_id):
    r = serializers.serialize('json', TaskResult.objects.filter(task_id=task_id))
    r = json.loads(r)
    return r


def query_task(task_name=None):
    if not task_name:
        r = list(PeriodicTask.objects.all())
        result = []
        for i in r:
            result.append({'name': i.name, 'enabled': i.enabled, 'task': i.task, })
    else:
        r = serializers.serialize('json', TaskResult.objects.filter(name=task_name))
        result = json.loads(r)
        return result


def delete_task(task_name):
    try:
        PeriodicTask.objects.filter(name=task_name).delete()
    except Exception as e:
        return (False, e)
    return (True, None)


def enable_task(task_name):
    try:
        task = PeriodicTask.objects.get(name=task_name)
        if not task.enabled:
            task.enabled = True
            task.save()
        else:
            pass
    except Exception as e:
        return (False, e)
    return (True, None)


def disable_task(task_name):
    try:
        task = PeriodicTask.objects.get(name=task_name)
        if not task.enabled:
            task.enabled = False
            task.save()
        else:
            pass
    except Exception as e:
        return (False, e)
    return (True, None)
