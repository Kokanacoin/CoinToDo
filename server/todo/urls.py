from django.urls import path
from . import views

urlpatterns = [
    path('test_api/', views.TestApi.as_view()),
    path('getUserList/', views.GetUserList.as_view()),
    path('getSettingTodoList/', views.GetSettingTodoList.as_view()),
    path('createNewTodo/', views.CreateNewTodo.as_view()),
    path('fixTodo/', views.FixTodo.as_view()),
    path('deleteTodo/', views.DeleteTodo.as_view()),
    path('getEverydayTodo/', views.GetEverydayTodo.as_view()),
    path('checkEverydayTodo/', views.CheckEverydayTodo.as_view()),
    path('getStatisticData/', views.GetStatisticData.as_view()),
    
    

    


]
