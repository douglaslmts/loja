from django.contrib import admin
from django.urls import path, include
from loja import views

urlpatterns = [
    path('',views.home_loja, name="home_loja"),
    path('erp/', include('ERP.urls')),
    path('app/', include('appStore.urls')),
    path('admin/', admin.site.urls),
]
