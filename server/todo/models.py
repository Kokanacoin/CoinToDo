from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32, unique=True)

class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    work_name = models.CharField(max_length=200)
    work_user = models.CharField(max_length=32)
    create_time=models.DateTimeField(auto_now_add=True) 
    update_time=models.DateTimeField(auto_now=True)
    use_state =  models.CharField(max_length=32)

class TodoHistory(models.Model):
    id = models.AutoField(primary_key=True)
    work_name = models.CharField(max_length=200)
    work_user = models.CharField(max_length=32)
    create_time=models.DateTimeField(auto_now_add=True)
    finish_time=models.DateTimeField(null=True)
    finish_state = models.BooleanField()
    