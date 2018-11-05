from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Craft(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def Member(self):
        return self.profile_set.all()

    def __str__(self):
        return "%s" % (self.name)
