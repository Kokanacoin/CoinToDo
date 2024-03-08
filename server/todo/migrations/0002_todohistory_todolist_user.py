# Generated by Django 3.2.8 on 2021-11-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('work_name', models.CharField(max_length=200)),
                ('work_user', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField(null=True)),
                ('finish_state', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('work_name', models.CharField(max_length=200)),
                ('work_user', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('use_state', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]