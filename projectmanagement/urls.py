"""
URL configuration for projectmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import authentication.views
import projectmanage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', projectmanage.views.home, name='home'),
    path('home/projects/', projectmanage.views.project_list, name='project-list'),
    path('home/projects/<int:project_id>/', projectmanage.views.project_detail, name='project-detail'),
    path('home/projects/<int:project_id>/delete/', projectmanage.views.project_delete, name='project-delete'),
    path('home/projects/<int:project_id>/tasks/<int:task_id>/', projectmanage.views.project_detail_task, name='project-detail-task'),
    path('home/projects/<int:project_id>/tasks/<int:task_id>/delete/', projectmanage.views.task_delete, name='task-delete'),
    path('home/new_project/', projectmanage.views.create_project, name='new-project'),
    path('home/new_task/', projectmanage.views.create_task, name='new-task'),
    path('home/assigned_tasks/', projectmanage.views.assigned_tasks, name='assigned-tasks'),
    path('home/assigned_tasks/update/<int:task_id>/', projectmanage.views.update_task, name='update-task'),
]
