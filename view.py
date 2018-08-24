# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:view.py
@Ide:PyCharm
@Time:2018/8/22 14:38
@Remark:
"""
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from celeryConfig.celeryBaseUtils import *
from celeryConfig import tasks

import json, os

os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def add_task(request):
    data = json.loads(request.body.decode('utf-8'))
    ttype = data.get('type')
    task_func = data.get('task_func')
    task_name = data.get('task_name')
    args = data.get('args', [])
    kwargs = data.get('kwargs', [])
    try:
        if ttype and ttype == 'interval':
            every = int(data.get('every'))
            interval_type = data.get('interval_type')
            schedule = get_or_create_interval(interval_type=interval_type,
                                              interval=every)
        elif ttype and ttype == 'crontab':
            execute_time = data.get('every')
            schedule = get_or_create_crontab(execute_time)
        result = create_task(schedule, task_name, 'celeryConfig.tasks.' + task_func, *args, **kwargs)
    except Exception as e:
        return JsonResponse(
            {"code": 404, "message": "error", "description": e.__str__()}, safe=False
        )
    if result[0]:
        return JsonResponse(
            {"code": 200, "message": "OK", "description": "success"}, safe=False
        )
    else:
        return JsonResponse(
            {"code": 404, "message": "error", "description": result[1].__str__()}, safe=False
        )


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def execute_task_by_name(request):
    data = json.loads(request.body.decode('utf-8'))
    task_func = data.get('task_func')
    args = data.get('args', [])
    kwargs = data.get('kwargs', [])
    if task_func:
        try:
            func = getattr(tasks,task_func)

        except AttributeError:
            return JsonResponse(
                {"code": 404, "message": "error", "description": "not task function"}
            )

        try:
            task = func.delay(*args,**kwargs)

        except Exception as e:
            return JsonResponse(
                {"code": 404, "message": "error", "description": e.__str__()}, safe=False
            )

        return JsonResponse(
            {"code": 200, "message": "OK", "description":task.id}, safe=False
        )


@require_http_methods(['GET'])
def query_task_by_id(request):
    task_id = request.GET.get('task_id')
    try:
        result = query_result(task_id)

    except Exception as e:
        return JsonResponse(
            {"code": 404, "message": "error", "description":"not task function"}, safe=False
        )

    return JsonResponse(
        {"code": 200, "message": "OK", "description":result}, safe=False
    )

@login_required
@require_http_methods(['GET'])
def query_task_by_taskname(request):
    task_name = request.GET.get('task_name')
    try:
        result = query_task(task_name)

    except Exception as e:
        return JsonResponse(
            {"code": 404, "message": "error", "description": e.__str__()}, safe=False
        )

    return JsonResponse(
        {"code": 200, "message": "OK", "description":result}, safe=False
    )


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def switch_task_by_name(request):
    data = json.loads(request.body.decode('utf-8'))
    task_name = data.get('task_name')
    status = data.get('status')
    if task_name and status:
        if status == 'true':
            result = enable_task(task_name)
        elif status == 'false':
            result = disable_task(task_name)
        else:
            return JsonResponse(
                {"code": 404, "message": "error", "description": "not support status"}, safe=False
            )
        if result[0]:
            return JsonResponse(
                {"code": 200, "message": "OK", "description": "success"}, safe=False
            )
        else:
            return JsonResponse(
                {"code": 404, "message": "error", "description": result[1].__str__()}, safe=False
            )
    return JsonResponse(
        {"code": 404, "message": "error", "description": "not support status"}
    )


@login_required
@require_http_methods(['GET'])
def delete_task_by_taskname(request):
    task_name = request.GET.get('task_name')
    if task_name:
        result = delete_task(task_name)
        if result[0]:
            return JsonResponse(
                {"code": 200, "message": "OK", "description": "success"}, safe=False
            )
        else:
            return JsonResponse(
                {"code": 404, "message": "error", "description": result[1].__str__()}, safe=False
            )
    else:
        return JsonResponse(
            {"code": 404, "message": "error", "description": "not task_name args"}
        )




