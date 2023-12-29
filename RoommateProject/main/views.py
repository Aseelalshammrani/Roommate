from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.models import Favorite, Profile, Validation
from advertisements.models import Advertisement,Advertisement_Image, Rent_Request
from django.contrib.auth.models import User
from django.db.models import Q



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
    costs = Advertisement.objects.all().order_by('price')
    return render(request,"main/cost_page.html",{"costs":costs})

def cost_more_filter_view(request:HttpRequest):
    costs = Advertisement.objects.all().order_by('-price')
    return render(request,"main/cost_page.html",{"costs":costs})


def is_valid_queryparam(param):
    return param != '' and param is not None

def advertisement_filter_view(request:HttpRequest):
    adv = Advertisement.objects.all()
    title = request.GET.get('title')
    duration_residence = request.GET.get('duration_residence')
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    number_of_people = request.GET.get('number_of_people')
    city = request.GET.get('city')
    has_kitchen = request.GET.get('has_kitchen')
    bathroom = request.GET.get('bathroom')
    dishwasher = request.GET.get('dishwasher')
    washing_machine = request.GET.get('washing_machine')
    neighborhood = request.GET.get('neighborhood')
    smoke_allowed = request.GET.get('smoke_allowed')
    type_of_residential = request.GET.get('type_of_residential')
    type_of_duration = request.GET.get('type_of_duration')
    animal_allowed = request.GET.get('animal_allowed')
    rooms_number = request.GET.get('rooms_number')
    gender = request.GET.get('gender')

    if is_valid_queryparam(title):
        adv = adv.filter(title__icontains=title)
    elif is_valid_queryparam(duration_residence):
        adv = adv.filter(duration_residence__icontains=duration_residence)
    elif is_valid_queryparam(number_of_people):
        adv = adv.filter(number_of_people__icontains=number_of_people)
    elif is_valid_queryparam(city):
        adv = adv.filter(city__icontains=city)
    elif is_valid_queryparam(has_kitchen):
        adv = adv.filter(has_kitchen__icontains=has_kitchen)
    elif is_valid_queryparam(bathroom):
        adv = adv.filter(bathroom__icontains=bathroom)
    elif is_valid_queryparam(dishwasher):
        adv = adv.filter(dishwasher__icontains=dishwasher)
    elif is_valid_queryparam(washing_machine):
        adv = adv.filter(washing_machine__icontains=washing_machine)
    elif is_valid_queryparam(neighborhood):
        adv = adv.filter(neighborhood__icontains=neighborhood)
    elif is_valid_queryparam(smoke_allowed):
        adv = adv.filter(smoke_allowed__icontains=smoke_allowed)
    elif is_valid_queryparam(type_of_residential):
        adv = adv.filter(type_of_residential__icontains=type_of_residential)
    elif is_valid_queryparam(type_of_duration):
        adv = adv.filter(type_of_duration__icontains=type_of_duration)
    elif is_valid_queryparam(animal_allowed):
        adv = adv.filter(animal_allowed__icontains=animal_allowed)
    elif is_valid_queryparam(rooms_number):
        adv = adv.filter(rooms_number__icontains=rooms_number)
    elif is_valid_queryparam(gender):
        adv = adv.filter(gender__icontains=gender)
    #min age
    if is_valid_queryparam(min_age):
        adv = adv.filter(min_age__icontains=min_age)
    #max age
    if is_valid_queryparam(max_age):
        adv = adv.filter(max_age__icontains=max_age)
    #price
    if is_valid_queryparam(price_min):
        adv = adv.filter(price__gte=price_min)
    if is_valid_queryparam(price_max):
        adv = adv.filter(price__lte=price_max)

    context = {
        'queryset':adv
    }
    return render(request, 'main/filter_page.html', context)

def not_found(request:HttpRequest):
    return render(request,'main/not_found.html')

def not_authorized(request:HttpRequest):
    return render(request,'main/not_authorized.html')

