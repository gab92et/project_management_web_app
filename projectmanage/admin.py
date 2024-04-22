from django.contrib import admin
from projectmanage.models import Project, Task, Worker


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'start_date', 'due_date')

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'due_date', 'project')


class WorkerAdmin(admin.ModelAdmin):
	list_display = ('user', 'is_manager')



admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Worker, WorkerAdmin)

