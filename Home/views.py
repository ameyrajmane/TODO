from django.shortcuts import render
from Home.models import Task


# Create your views here.


def Home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        task = Task(taskTitle=title, taskDesc=desc)
        task.save()
        context = {'success': True}

    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)
