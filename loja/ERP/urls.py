from django.contrib import admin
from django.urls import path
from ERP import views

urlpatterns = [
    path('',views.home_erp, name="home_erp"),
]
