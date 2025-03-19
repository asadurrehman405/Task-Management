from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm
import json



@csrf_exempt
def task_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = TaskForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "task created successfully"}, status=201)
        return JsonResponse({"error": "Invalid data"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
@csrf_exempt
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        form = TaskForm(data, instance=task)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "task updated successfully"})
        return JsonResponse({"error": "Invalid data"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
@csrf_exempt
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({"message": "task deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)

def task_toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'completed' if task.status == 'pending' else 'pending'
    task.save()
    return JsonResponse({"message": "Task status updated successfully"}, safe=False)  # ✅ Return a dictionary
