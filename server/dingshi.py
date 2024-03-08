import sys
import os

# 获取当前文件的目录
pwd = os.path.dirname(os.path.realpath(__file__))
# 获取当前项目名的目录(因为我的当前文件是在项目名下的文件夹下的文件.所以是../)
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")


import django
django.setup()
from todo.models import TodoList, TodoHistory
def time_task():
    # 新建history
    #错的
    # all_todo = TodoList.objects.all()
    #对的
    all_todo = TodoList.objects.filter(use_state="using")
    for each in all_todo:
        TodoHistory.objects.create(**{
            'work_user': each.work_user,
            'work_name': each.work_name,
            'finish_state': False
        })

time_task()
