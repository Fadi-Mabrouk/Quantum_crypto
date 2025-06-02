from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('code/', views.current_code, name='current_code'),
    path('verify/', views.verify_code, name='verify_code'),
]