# celery
celery
1 安装redis
2 安装celery相关模块
pip3 install redis celery  django_celery_beat django_celery_results
3 引入app，加入到settings.py
  INSTALLED_APPS = [
  ... ...
  'django_celery_beat',
  'django_celery_results',
  ]
  4 在项目中引入celeryConfig app
    启动celery相关进程
    启动worker及beat:
    celery multi start worker -A celeryConfig.app -B -c 4 --pidfile=/tmp/celery.id --logfile=/tmp/celery.log
    关闭worker及beat:
    celery multi stopwait worker -A celeryConfig.app -B -c 4 --pidfile=/tmp/celery.id --logfile=/tmp/celery.log
