from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name=""),
    path('home/', views.home, name=""),
    path('login/', views.login, name="login"),
    path('register_patient/', views.register_patient, name="register_patient"),
]