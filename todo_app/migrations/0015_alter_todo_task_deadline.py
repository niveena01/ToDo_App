# Generated by Django 4.2.2 on 2023-12-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0014_alter_todo_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_task',
            name='deadline',
            field=models.DateTimeField(blank=True),
        ),
    ]