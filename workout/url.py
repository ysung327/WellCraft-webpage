from django.urls import path
from .import views

app_name = 'workout'

urlpatterns = [
    path('my-workout/', views.my_workout_view, name="my-workout"),
    path('ajax/load_workout_list/', views.load_workout_list, name="load-workout-list"),
]
