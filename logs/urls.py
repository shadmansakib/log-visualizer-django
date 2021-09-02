from django.urls import path

from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.visualize, name='dashboard'),
    path('chart/category/', views.category_count, name='category-count'),
    path('chart/log-count/', views.log_count, name='log-count'),
]
