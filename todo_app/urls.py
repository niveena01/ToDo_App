from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_create, name='task_create'),
    path('list/',views.task_list,name='task_list'),
    path('update/<pk>',views.task_edit,name='task_update'),
    path('delete/<pk>',views.task_delete,name='task_delete'),
    
]