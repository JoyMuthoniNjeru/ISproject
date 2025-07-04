from django.db import models
from django.contrib.auth.models import User

class TestCentre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

