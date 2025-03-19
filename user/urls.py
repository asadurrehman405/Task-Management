from django.urls import path
from .views import task_list, task_create, task_update, task_delete, task_toggle_status

urlpatterns = [
    path('task_list/', task_list, name='task_list'),
    path('task_create/', task_create, name='task_create'),
    path('task_update/<int:task_id>/', task_update, name='task_update'),
    path('task_delete/<int:task_id>/', task_delete, name='task_delete'),
    path('task_toggle_status/<int:task_id>/', task_toggle_status, name='task_toggle_status'),
]
