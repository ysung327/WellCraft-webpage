from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('my-account/', views.my_account_view, name="my-account"),
    path('login-register/', views.login_register_view, name="login-register"),
    path('my-profile/', views.my_profile_view, name="my-profile"),
    path('my-profile/register/', views.register_profile_view, name="register-profile"),
    path('logout/', views.logout_view, name="logout"),
]