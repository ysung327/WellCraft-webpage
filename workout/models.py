from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .myField import DayOfTheWeekField, NumberOfTheWeekField
from workout_info.models import WorkoutInfo
import datetime


# Create your models here.
class Plan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


# Plan model's receiver
@receiver(post_save, sender=User)
def create_user_plan(sender, instance, created, **kwargs):
    if created:
        Plan.objects.create(user=instance)  # user instance 생성되면 profile 자동으로 생성

@receiver(post_save, sender=User)
def update_user_plan(sender, instance, **kwargs):
    instance.plan.save()


class Week(models.Model):
    monday = models.DateField(null=True) #월요일 날짜로 저장.
    number = NumberOfTheWeekField(null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['monday']

    def AutoCreate(self):  # 서버에서 월요일이 되면 자동적으로 생성??
        pass

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        dict = MonthWeekNum(now)
        self.monday = dict['monday']
        self.number = dict['weekNum']
        super(Week, self).save()

    def __str__(self):
        return "%d년 %d월 %d주" % (self.monday.year, self.monday.month, self.number)


class Day(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    day = DayOfTheWeekField(null=True, blank=True)
    done = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ['day']

    def __str__(self):
        return "%d년 %d월 %d일 %s" % (self.date.year, self.date.month, self.date.day, self.day)


class WorkoutLog(models.Model):
    log = models.FileField(null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)


class Exercise(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)
    workout_info = models.ForeignKey(WorkoutInfo, null=True, on_delete=models.CASCADE)
    set = models.IntegerField(null=True, blank=True)
    times = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.workout_info


def MonthWeekNum(now):
    nowTuple = now.timetuple()
    mon = nowTuple.tm_mon
    day = nowTuple.tm_yday
    weekDay = nowTuple.tm_wday
    monday = now - datetime.timedelta(days=weekDay)
    mondayTuple = monday.timetuple()
    cnt = 0
    if mon != mondayTuple.tm_mon:
        while mondayTuple.tm_mon <= mon - 1:
            monday = monday - datetime.timedelta(weeks=1)
            mondayTuple = monday.timetuple()
            cnt = cnt + 1
            if mondayTuple.tm_mon == mon - 2:
                mon = mon - 1
                break
    else:
        while mondayTuple.tm_mon <= mon:
            monday = monday - datetime.timedelta(weeks=1)
            mondayTuple = monday.timetuple()
            cnt = cnt + 1
            if mondayTuple.tm_mon == mon - 1:
                break
    weekNum = cnt
    dict = {
        'mon': mon,
        'monday': monday,
        'weekNum': weekNum,
    }
    return dict


