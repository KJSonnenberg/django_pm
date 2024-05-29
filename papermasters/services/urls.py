from django.urls import path
from . import views
from .views import (index, )

app_name = 'services'

urlpatterns = [
    path('', views.index, name = 'index')
    ]