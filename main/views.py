from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Введены некорректные данные'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', context)
