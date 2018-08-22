# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:tasks.py
@Ide:PyCharm
@Time:2018/8/22 11:28
@Remark:celery需要注册的任务（项目中需要在celery中运行的函数），
        这里只是测试用例，*args为位置参数（列表），**kwargs为关键字参数（字典），通过接口传递。
"""

from celery.signals import  task_failure,task_success
from .app import app
from .projectTasks import *

@app.task(bind=True,max_retries=3,default_retry_delay=30)
def test(self,*args,**kwargs):
    return args

@app.task(max_retries=3,default_retry_delay=30)
def add(x,y):
    return x+y

@task_failure.connect
def task_fail_handler(*args,**kwargs):
    pass

@task_success.connect
def task_success_handler(*args,**kwargs):
    pass


@app.task(max_retries=3,default_retry_delay=30)
def check_projecttask_plan(*args,**kwargs):
    result = projectConfig()
    return result
