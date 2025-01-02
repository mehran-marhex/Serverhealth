from django.urls import path
from os_data_storage.views import os_data_storage
from . import views


os_data_storage()


urlpatterns = [
    path("", views.index, name="index"),
]
