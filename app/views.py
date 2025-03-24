from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def index(request):
    if request.method == 'POST':
        text = request.POST.get('task')
        if text:
            Task.objects.create(text=text)
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'detail.html', {'task': task})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.text = request.POST.get('task')
        task.save()
        return redirect('index')
    return render(request, 'edit.html', {'task': task})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')