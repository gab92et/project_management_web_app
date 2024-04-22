from django.db import models
from authentication.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    
    class TaskStatus(models.TextChoices):
        NON_STARTED = 'NS'
        IN_PROGRESS = 'IP'
        COMPLETED = 'CP'
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.fields.CharField(choices=TaskStatus.choices, default= 'NS',max_length=5)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    advancement = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.title




