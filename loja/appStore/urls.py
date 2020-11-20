from django.urls import path
from appStore import views

urlpatterns = [
    path('', views.home_app, name="home_app"),
]
