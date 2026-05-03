from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required(login_url='/admin')
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(user=request.user, title=title)
        return redirect('/')

    tasks = Task.objects.filter(user=request.user).order_by('-created')
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)