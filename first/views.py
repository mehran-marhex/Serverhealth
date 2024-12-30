from django.shortcuts import render
from django.http import HttpResponse
import psutil
import time

# Create your views here.

def index(request):
    cpu_percent = 0
    for x in range(20):
        cpu_percent = psutil.cpu_percent()
        return HttpResponse(f"CPU Percent is => {cpu_percent}")
        time.sleep(1)
