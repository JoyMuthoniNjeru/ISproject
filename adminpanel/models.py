from django.db import models
from testcentre.models import TestCentre

class TestSlot(models.Model):
    test_centre = models.ForeignKey(TestCentre, on_delete=models.CASCADE)
    date = models.DateField()
    time_range = models.CharField(max_length=100)
    max_applicants = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.test_centre.name} on {self.date} at {self.time_range}"

