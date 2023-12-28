from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.models import Favorite, Profile, Validation
from advertisements.models import Advertisement,Advertisement_Image, Rent_Request
from django.contrib.auth.models import User



#Home page view
def home_page(request:HttpRequest):
    advertisements = Advertisement.objects.all()[0:6]
    return render(request,"main/home.html",{"advertisements":advertisements})

#Filter all the genders advertisements
def advertisements_genders_view(request: HttpRequest):
    advertisements = Advertisement.objects.all()
    return render(request,"main/gender_page.html", {"advertisements" : advertisements})

#Filter only the female gender advertisements
def advertisements_female_gender_view(request: HttpRequest):
    advertisements = Advertisement.objects.filter(gender='Female')
    return render(request,"main/gender_page.html", {"advertisements" : advertisements})

#Filter only the male gender advertisements
def advertisements_male_gender_view(request: HttpRequest):
    advertisements = Advertisement.objects.filter(gender='Male')
    return render(request,"main/gender_page.html", {"advertisements" : advertisements})


def cost_view(request:HttpRequest):
    costs = Advertisement.objects.all()
    return render(request,"main/cost_page.html",{"costs":costs})

def cost_less_filter_view(request:HttpRequest):
    costs = Advertisement.objects.filter(price__lte=1900)
    return render(request,"main/cost_page.html",{"costs":costs})

def cost_more_filter_view(request:HttpRequest):
    costs = Advertisement.objects.filter(price__gte=1900)
    return render(request,"main/cost_page.html",{"costs":costs})

