from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Advertisement 


def add_advertisement(request:HttpRequest):
    return render (request,'advertisements/add_advertisement.html',{'types_of_gender':Advertisement.types_of_gender,'types_of_residential':Advertisement.types_of_residential,'types_of_duration':Advertisement.types_of_duration})
# Create your views here.