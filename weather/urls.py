from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='weather_home'),
   path('weekly/', views.weekly, name='weather_weekly'),

]
