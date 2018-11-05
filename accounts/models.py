from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from craft.models import Craft

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=32, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=32, null=True, blank=True)
    frequency = models.CharField(max_length=32, null=True, blank=True) #매일, 주 5회이상, 주 3회이상, 주 1회.
    aim = models.CharField(max_length=32, null=True, blank=True) #다이어트, 벌크업, 건강유지. 패션헬스
    goal = models.FloatField(null=True, blank=True) #정확한 수치. aim이 뭐냐에 따라 다르게 출력.
    #craft = models.ForeignKey(Craft, null=True, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return "%s" % self.user

    def Weight(self):
        return self.weight

    def Height(self):
        return self.height


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #user instance가 생성되면 profile 자동으로 생성


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.profile.save() #profile의 정보 저장. 사실상 안되는 코드.
