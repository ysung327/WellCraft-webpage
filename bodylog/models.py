from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.
class BodyLog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    weight = Profile.Weight(user.profile)
    height = Profile.Height(user.profile)
    muscle_mass = models.FloatField(null=True, blank=True) #골격근량
    fat_mass = models.FloatField(null=True, blank=True) #체지방량
    percent_body_fat = models.FloatField(null=True, blank=True) #체지방률
    '''여기부터'''
    body_water = models.FloatField(null=True, blank=True) #체수분
    protein = models.FloatField(null=True, blank=True) #단백질
    '''여기까지 근육량'''
    mineral = models.FloatField(null=True, blank=True) #무기질
    '''여기까지 합이 제지방량'''
    '''여기에 fat_mass 합치면 체중'''

