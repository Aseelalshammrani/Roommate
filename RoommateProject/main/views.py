from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.models import Favorite, Profile, Validation



def home_page(request:HttpRequest):
    return render(request,'main/home.html')


def approve_accounts_view(request:HttpRequest):

    approves = Validation.objects.filter(validated=True)

    return render(request,"main/home.html",{"approves":approves})
