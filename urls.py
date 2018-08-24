# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:urls.py
@Ide:PyCharm
@Time:2018/8/22 14:39
@Remark:
"""

from django.conf.urls import url

from . import view

app_label = 'project'

urlpatterns = [
    url(r'^project/add_task/$', view.add_task),  # 添加任务
    url(r'^project/execute_task/$', view.execute_task_by_name),  # 异步任务执行
    url(r'^project/query_id/$', view.query_task_by_id),  # 异步结果查询
    url(r'^project/switch_task/$', view.switch_task_by_name),  # 启用禁用任务
    url(r'^project/query_name/$', view.query_task_by_taskname),  # 查看已建立的任务
    url(r'^project/delete_task/$', view.delete_task_by_taskname),  # 删除已建立的任务
]
