from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
    members = models.ManyToManyField(User, related_name='projects', blank=True)
