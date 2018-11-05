from django.db import models
from .myField import PartOfTheWorkout, EngNameOfTheWorkout

# Create your models here.
class Part(models.Model):
    kor_name = PartOfTheWorkout(null=True, blank=True)
    eng_name = EngNameOfTheWorkout(null=True, blank=True)

    def __str__(self):
        return "%s" % PartOfTheWorkout.get_part_name(self.kor_name)


class WorkoutInfo(models.Model):
    eng_name = models.CharField(max_length=32, null=True, blank=True)
    kor_name = models.CharField(max_length=32, null=True, blank=True)
    how = models.TextField(max_length=1000, null=True, blank=True)
    part = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.kor_name

