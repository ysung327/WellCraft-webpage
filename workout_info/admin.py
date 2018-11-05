from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Part, WorkoutInfo

admin.site.register(Part)
admin.site.register(WorkoutInfo)
