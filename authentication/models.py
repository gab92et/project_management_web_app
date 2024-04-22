from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

	MANAGER = 'MANAGER'
	WORKER = 'WORKER'

	ROLE_CHOICES = (
		(MANAGER, 'Manager'),
		(WORKER, 'Worker'))
	profile_photo = models.ImageField(verbose_name='Profile picture',null=True,blank=True )
	role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')