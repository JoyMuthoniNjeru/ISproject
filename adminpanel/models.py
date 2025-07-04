from django.db import models
from testcentre.models import TestCentre

class TestSlot(models.Model):
    test_centre = models.ForeignKey(TestCentre, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_applicants = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.test_centre.name} – {self.date} ({self.start_time}-{self.end_time})"

