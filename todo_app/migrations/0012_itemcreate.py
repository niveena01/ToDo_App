# Generated by Django 4.2.2 on 2023-12-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0011_todoitem_delete_todoitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('deadline', models.DateField(blank=True)),
                ('status', models.CharField(choices=[('not_started', 'Not started'), ('in_progress', 'In progress'), ('completed', 'Completed'), ('postponed', 'Postponed'), ('cancelled', 'Cancelled')], default='not_started', max_length=20)),
            ],
        ),
    ]
