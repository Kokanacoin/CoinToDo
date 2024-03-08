from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import User, TodoList, TodoHistory
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import math
'''
    开启定时工作
'''

# def openDing():
    
#     try:
#         # 实例化调度器
#         scheduler = BackgroundScheduler()
#         # 调度器使用DjangoJobStore()
#         scheduler.add_jobstore(DjangoJobStore(), "default")

#         @register_job(scheduler, 'cron', day_of_week='mon-sun', hour='00', minute='00', second='10',id='time_task')
#         def time_task():
#             #新建history
#             all_todo = TodoList.objects.all()
#             for each in all_todo:
#                 TodoHistory.objects.create(**{
#                     'work_user': each.work_user,
#                     'work_name': each.work_name,
#                     'finish_state': False
#                 })
#         register_events(scheduler)
#         # scheduler.start()
#         scheduler.remove_job(time_task)
#     except Exception as e:
#         print('2'*50)
#         print(e)
#         scheduler.shutdown()

# # openDing()

class TestApi(View):
    def get(self, request):
        User.objects.create(**{'user_name': '小黄鱼'})
        res = {
            'state': 'OK'
        }
        return JsonResponse(res)

    def post(self, request):
        data = [
            {
                "name": "奔奔",
                "age": 18
            },
            {
                "name": "小小",
                "age": 20
            }
        ]
        # 返回字典，需要使用JsonResponse
        # 如果返回的非字典，需要设置safe=False
        return JsonResponse(data, safe=False)


'''
    获取用户列表
'''


class GetUserList(View):
    def post(self, request):
        res = {
            'state': 'OK',
            'data': {
                'user_name': [{'label': x.user_name, 'value': x.user_name} for x in User.objects.all()]
            }
        }
        return JsonResponse(res)


'''
    获取todolist设置列表
'''


class GetSettingTodoList(View):
    def post(self, request):

        user_name = request.POST['user_name']
        res_data = TodoList.objects.filter(
            work_user=user_name).filter(use_state='using')
        res = {'state': 'OK',
               'data': {'data_name': [x.work_name for x in res_data],
                        'id': [[x.id for x in res_data]]}
               }
        return JsonResponse(res)


class CreateNewTodo(View):
    def post(self, request):

        user_name = request.POST['user_name']
        new_todo = request.POST['new_todo']
        res_data = TodoList.objects.filter(
            work_user=user_name).filter(work_name=new_todo)

        if len(res_data) > 0:
            print(res_data)
            if res_data[0].use_state == "delete":
                res_data = TodoList.objects.filter(
                    work_user=user_name).filter(work_name=new_todo).update(use_state='using')
                res = {'state': 'OK',
                       'message': '新增todo成功！'
                       }
            else:
                res = {
                    'state': 'NG',
                    'message': '已经存在了这个了'
                }
        else:
            TodoList.objects.create(**{
                'work_name': new_todo,
                'work_user': user_name,
                'use_state': 'using'
            })

            res = {'state': 'OK',
                   'message': '新增todo成功！'
                   }

        # 这里还要刷新每日的任务
        if res['state'] == "OK":
            TodoHistory.objects.create(**{
                'work_user': user_name,
                'work_name': new_todo,
                'finish_state': False
            })

        return JsonResponse(res)


class FixTodo(View):
    def post(self, request):

        user_name = request.POST['user_name']
        new_todo = request.POST['new_todo']
        old_todo = request.POST['old_todo']
        res_data = TodoList.objects.filter(
            work_user=user_name).filter(work_name=new_todo)

        if len(res_data) > 0:
            res = {
                'state': 'NG',
                'message': '已经存在了这个了'
            }
        else:
            TodoList.objects.filter(work_name=old_todo).filter(
                work_user=user_name).update(work_name=new_todo)
            # TODO:
            # 这里还要刷新每日的任务
            res = {'state': 'OK',
                   'message': '修改todo成功！'
                   }
        return JsonResponse(res)


class DeleteTodo(View):
    def post(self, request):

        user_name = request.POST['user_name']
        old_todo = request.POST['old_todo']
        TodoList.objects.filter(work_name=old_todo).filter(
            work_user=user_name).update(use_state='delete')
        res = {
            'state': 'OK',
            'message': '删除todo成功！'
        }
        return JsonResponse(res)


class GetEverydayTodo(View):
    def post(self, request):
        # 搜寻当天的
        now_user = request.POST['now_user']
        d1 = timezone.now()
        year = d1.strftime("%Y-%m-%d").split('-')[0]
        month = d1.strftime("%Y-%m-%d").split('-')[1]
        day = d1.strftime("%Y-%m-%d").split('-')[2]
        res_data = TodoHistory.objects.filter(work_user=now_user).filter(create_time__year=year).filter(
            create_time__month=month).filter(create_time__day=day)
        res = {
            'state': 'OK',
            'data': [{'work_name': x.work_name, 'check_state': bool(x.finish_state)} for x in res_data],
            'today': d1.strftime("%Y-%m-%d")
        }
        return JsonResponse(res)


class CheckEverydayTodo(View):
    def post(self, request):
        now_user = request.POST['now_user']
        work_name = request.POST['work_name']
        check_state = request.POST['check_state']
        today = request.POST['today']

        year = today.split('-')[0]
        month = today.split('-')[1]
        day = today.split('-')[2]

        res = {
            'state': 'OK',
        }
        if check_state == 'true':
            check_state = True
        else:
            check_state = False

        if check_state == True:
            TodoHistory.objects.filter(work_user=now_user).filter(work_name=work_name).filter(create_time__year=year).filter(
                create_time__month=month).filter(create_time__day=day).update(**{'finish_state': check_state, 'finish_time': timezone.now()})
            res['message'] = "成功完成打卡✅"
        else:
            TodoHistory.objects.filter(work_user=now_user).filter(work_name=work_name).filter(create_time__year=year).filter(
                create_time__month=month).filter(create_time__day=day).update(**{'finish_state': check_state,
                                                                                 'finish_time': None})
            res['message'] = "取消打卡"
        print("!"*20, today)
        return JsonResponse(res)

class GetStatisticData(View):
     def post(self, request):
        now_user = request.POST['now_user']
        month = request.POST['date'].split('-')[1]
        year = request.POST['date'].split('-')[0]
        res_db = TodoHistory.objects.filter(**{
            "work_user":now_user,
            "create_time__year":year,
            "create_time__month":month
        }).all()
        month = str(int(month) - 1)
        data = {}
        for each in res_db:
            day = str(each.create_time.day)
            if "date_"+ month+"_"+day not in data.keys():

                data["date_"+ month+"_"+day] = []
                data["date_"+ month+"_"+day].append({})
                data["date_"+ month+"_"+day][0]['tooltips'] = []
                data["date_"+ month+"_"+day][0]['key'] = 1
            data["date_"+ month+"_"+day][0]['tooltips'].append({
                'task':each.work_name,
                'state':'error' if each.finish_state == 0 else 'success'
            })
        for each in data.keys():
            error, success = 0,0
            for each_tool_state in data[each][0]['tooltips']:
                if each_tool_state['state'] == 'error':
                    error += 1
                else:
                    success += 1
  
            data[each][0]['text'] = str(success)+ '/' + str(success+error)
            data[each][0]['persent'] = math.ceil((success/(success+error)) * 100)
        res = {
            'state':"OK",
            'data':data
        }
        return JsonResponse(res)
 
