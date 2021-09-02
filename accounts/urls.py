from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_user, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('change-password/', views.change_password, name='change-password'),

]
