from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.models import Favorite, Profile, Validation
from advertisements.models import Advertisement,Advertisement_Image, Rent_Request, Review
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def home_page(request: HttpRequest):
    advertisements = Advertisement.objects.all()[0:6]
    reviews = Review.objects.all().order_by("-rating")[0:4]

    context = {
        "advertisements": advertisements,
        "reviews": reviews,
    }

    return render(request, "main/home.html", context)


def is_valid_queryparam(param):
    return param != '' and param is not None

def advertisement_filter_view(request:HttpRequest):
    msg=None
    try:
        adv = Advertisement.objects.all()
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

        if is_valid_queryparam(duration_residence):
            adv = adv.filter(duration_residence__icontains=duration_residence)
        elif is_valid_queryparam(number_of_people):
            adv = adv.filter(number_of_people__icontains=number_of_people)
        elif is_valid_queryparam(city):
            adv = adv.filter(city__icontains=city)
        elif is_valid_queryparam(bathroom):
            adv = adv.filter(bathroom__icontains=bathroom)
        elif is_valid_queryparam(neighborhood):
            adv = adv.filter(neighborhood__icontains=neighborhood)
        elif is_valid_queryparam(type_of_residential):
            adv = adv.filter(type_of_residential__icontains=type_of_residential)
        elif is_valid_queryparam(rooms_number):
            adv = adv.filter(rooms_number__icontains=rooms_number)
        #gender
        if gender:
            adv = adv.filter(gender=gender)
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
        #type_of_duration
        if type_of_duration:
            adv = adv.filter(type_of_duration=type_of_duration)
        #has_kitchen
        if has_kitchen:
            adv = adv.filter(has_kitchen=True)
        #dishwasher
        if dishwasher:
            adv = adv.filter(dishwasher=True)
        #washing machine
        if washing_machine:
            adv = adv.filter(washing_machine=True)
        #Animal allowed
        if animal_allowed:
            adv = adv.filter(animal_allowed=True)
        #Animal allowed
        if smoke_allowed:
            adv = adv.filter(smoke_allowed=True)
    except Exception as e:
        msg=f'Something went wrong:{e}'
    context = {
        'Advertisements':adv,
        'types_of_gender': Advertisement.types_of_gender,
        'types_of_residential':Advertisement.types_of_residential,
        'types_of_duration': Advertisement.types_of_duration,
        'msg':msg,
    }
    return render(request, 'main/filter_page.html', context)

def not_found(request:HttpRequest):
    return render(request,'main/not_found.html')

def not_authorized(request:HttpRequest):
    return render(request,'main/not_authorized.html')


def contact_us_view(request):
    email_sent = False
    if request.method =='POST':
        message = request.POST["message"]
        email = request.POST["email"]
        name = request.POST['name']
        message_content = f" ({email}) sent you a message : \n Message content: {message}"
        send_mail(
            'Contact Form',#title
            message_content, #message
            'settings.EMAIL_HOST_USER', #Sender if not avalaible considered 
            ["sufanamarouf1@gmail.com"],#recive email
            fail_silently=False)
        
        email_sent = True
    return render(request,"main/contact_us.html", {"email_sent" : email_sent})



