from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Worker
from .forms import TaskForm, ProjectForm



@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # project = form.save(commit=False)
            # # project.manager = request.user
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm()
    return render(request, 'projectmanage/project_form.html', {'form': form})

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projectmanage/project_list.html', {'projects': projects})


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projectmanage/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def home(request):
	return render(request, 'projectmanage/home.html')



@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'projectmanage/task_form.html', {'form': form})



@login_required
def project_detail_task(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'projectmanage/project_detail_task.html', {'project': project, 'task': task})


# @login_required
# def task_detail(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     # task = Task.objects.get(pk=task_id)
#     return render(request, 'projectmanage/task_detail.html', {'task': task})


@login_required
def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        # update task advancement percentage
        task.advancement = request.POST.get('advancement')
        if int(task.advancement) == 0:
        	task.status = 'NS'
        elif int(task.advancement) < 100:
        	task.status = 'IP'
        else:
        	task.status = 'CP'
        task.save()
        return redirect('assigned-tasks')
    return render(request, 'projectmanage/update_task.html', {'task': task})


@login_required
def assigned_tasks(request):

    tasks = Task.objects.filter(worker=request.user.worker)
    worker = request.user.worker
    return render(request, 'projectmanage/assigned_tasks.html', {'tasks': tasks, 'worker':worker})


@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project-list')
    return render(request, 'projectmanage/project_delete.html', {'project': project})

@login_required
def task_delete(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'projectmanage/task_delete.html', {'project': project, 'task': task})


