# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import health_check, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('', home, name='home'),
]