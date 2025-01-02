from django.urls import path
from os_data_storage.views import os_data_storage
from . import views
from os_data_storage.counter.main import startProject


startProject()


urlpatterns = [
    path("", views.index, name="index"),
]
