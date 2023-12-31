from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Advertisement, Rent_Request, Advertisement_Image ,Review
from django.contrib.auth.models import User
from accounts.models import Favorite, Profile, Validation
from django.db.models import Avg, Sum, Max, Min
from django.core.exceptions import ValidationError
# Create your views here.

#Add a new advertisement
def add_advertisement_view(request:HttpRequest):
    msg = None
    try:
        if not request.user.is_authenticated:
            return redirect('main:not_authorized')
        if request.method == "POST":
            advertisement = Advertisement(
            user = request.user,
            title = request.POST["title"],
            image = request.FILES["image"],
            type_of_duration = request.POST["type_of_duration"],
            duration_residence = request.POST["duration_residence"],
            type_of_residential = request.POST["type_of_residential"],
            longitude = request.POST["longitude"],
            latitiiude = request.POST["latitiiude"],
            space = request.POST["space"],
            price = request.POST["price"],
            number_of_people = request.POST["number_of_people"],
            min_age = request.POST["min_age"],
            max_age = request.POST["max_age"],
            gender = request.POST["gender"],
            note = request.POST["note"],
            rooms_number = request.POST["rooms_number"],
            bathroom = request.POST["bathroom"],
            city=request.POST['city'],
            neighborhood=request.POST['neighborhood']
            )
            if 'animal_allowed' in request.POST:
                advertisement.animal_allowed = request.POST["animal_allowed"]
            if 'smoke_allowed' in request.POST:
                advertisement.animal_allowed = request.POST["smoke_allowed"]
            if 'has_kitchen' in request.POST:
                advertisement.animal_allowed = request.POST["has_kitchen"]
            if 'approved_status' in request.POST:
                advertisement.animal_allowed = request.POST["approved_status"]
            if 'dishwasher' in request.POST:
                advertisement.dishwasher=request.POST['dishwasher']
            if 'washing_machine' in request.POST:
                advertisement.washing_machine=request.POST['washing_machine']
            advertisement.save()
            return redirect("advertisements:add_images_to_advertisements",advertisement_id=advertisement.id)
    except ValidationError as e:
        msg=f'Please Specify the location'
    except Exception as e:
        msg = f"Please ensure all required fields are complete and try again. {e}"
    return render (request,'advertisements/add_advertisement.html',{'types_of_gender':Advertisement.types_of_gender,'types_of_residential':Advertisement.types_of_residential,'types_of_duration':Advertisement.types_of_duration,'cities':Advertisement.cities,'msg':msg})

def browse_advertisements_view(request:HttpRequest):
    msg=None
    try:
        advertisements=Advertisement.objects.all()
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'advertisements/browse_advertisements.html',{'advertisements':advertisements,'msg':msg})


def advertisement_details_view(request:HttpRequest,advertisement_id):
    try:
        advertisement=Advertisement.objects.get(id=advertisement_id)
        is_requested=request.user.is_authenticated and Rent_Request.objects.filter(user=request.user,advertisement=advertisement).exists()
        advertisement_images=Advertisement_Image.objects.filter(advertisement=advertisement)
        is_favored = request.user.is_authenticated and Favorite.objects.filter(advertisement=advertisement, user=request.user).exists()
        reviews = Review.objects.filter(advertisement= advertisement)
        reviews_avg = Review.objects.filter(advertisement=advertisement).aggregate(Avg("rating"))["rating__avg"]
    except Exception:
        return redirect('main:not_found')
    return render(request,"advertisements/advertisement_details.html",{'advertisement':advertisement,'is_requested':is_requested,"is_favored":is_favored,'advertisement_images':advertisement_images,"reviews" : reviews,"reviews_avg": reviews_avg})


#Update advertisement
def update_advertisement_view(request:HttpRequest, advertisement_id):
    msg=None
    try:
        advertisement = Advertisement.objects.get(id=advertisement_id)
        if request.user != advertisement.user :
            return render(request,'main/not_authorized.html')
        if request.method == "POST":
            advertisement.title = request.POST["title"]
            if 'image' in request.FILES:
                advertisement.image = request.FILES["image"]
            advertisement.type_of_duration = request.POST["type_of_duration"]
            advertisement.duration_residence = request.POST["duration_residence"]
            advertisement.type_of_residential = request.POST["type_of_residential"]
            advertisement.space = request.POST["space"]
            advertisement.price = request.POST["price"]
            advertisement.number_of_people = request.POST["number_of_people"]
            advertisement.neighborhood=request.POST["neighborhood"]

            if 'animal_allowed' in request.POST:
                advertisement.animal_allowed = request.POST['animal_allowed']
            else:
                advertisement.animal_allowed = False
            if 'dishwasher' in request.POST:
                advertisement.dishwasher = request.POST['dishwasher']
            else:
                advertisement.dishwasher = False
                
            if 'smoke_allowed' in request.POST:
                advertisement.smoke_allowed = request.POST['smoke_allowed']
            else:
                advertisement.smoke_allowed = False

            if 'has_kitchen' in request.POST:
                advertisement.has_kitchen = request.POST['has_kitchen']
            else:
                advertisement.has_kitchen = False

            if 'washing_machine' in request.POST:
                advertisement.washing_machine = request.POST['washing_machine']
            else:
                advertisement.washing_machine = False

            if 'advertisement_status' in request.POST:
                advertisement.advertisement_status = request.POST['advertisement_status']
            else:
                advertisement.advertisement_status=True

            advertisement.min_age = request.POST["min_age"]
            advertisement.max_age = request.POST["max_age"]
            advertisement.gender = request.POST["gender"]
            advertisement.note = request.POST["note"]
            advertisement.rooms_number = request.POST["rooms_number"]
            advertisement.bathroom = request.POST["bathroom"]
            advertisement.save()
            return redirect("advertisements:advertisement_details_view", advertisement_id=advertisement.id)
    except Exception as e:
        msg = f"Please ensure all required fields are complete and try again. {e}"
    return render(request,"advertisements/update_advertisement.html", {"advertisement": advertisement,'types_of_duration':Advertisement.types_of_duration,'types_of_residential':Advertisement.types_of_residential,'types_of_gender':Advertisement.types_of_gender,'msg':msg})



def delete_advertisement_view(request:HttpRequest, advertisement_id):
    try:
        if request.user != advertisement.user :
                return render(request,'main/not_authorized.html')
        advertisement=Advertisement.objects.get(id=advertisement_id)
        advertisement.delete()
        return redirect("advertisements:browse_advertisements_view")
    except Exception as e:
        return redirect('main:not_authorized')
    
def search(request: HttpRequest):
    msg = None
    try:
        if 'search' in request.GET:
            query = request.GET['search']
            advertisements = Advertisement.objects.filter(neighborhood__contains=query)
        else:
            advertisements = Advertisement.objects.all()
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request, 'advertisements/search.html',  {"advertisements" : advertisements,'msg':msg})


def add_images_to_advertisements(request:HttpRequest, advertisement_id):
    msg = None
    try:
        advertisement=Advertisement.objects.get(id=advertisement_id)
        if request.user != advertisement.user :
            return render(request,'main/not_authorized.html')
        if request.method=='POST':
            advertisement_image=Advertisement_Image(advertisement=advertisement,image=request.FILES["image"])
            advertisement_image.save()
    except Exception as e:
        msg = f"Please ensure you upload images only.{e}"
    return render(request,'advertisements/add_image.html',{'advertisement':advertisement,'msg':msg})


def add_review_view(request: HttpRequest, advertisement_id):
    try:
        if not request.user.is_authenticated:
                return render(request, 'main/not_found.html')
        if request.method == "POST":
            advertisement= Advertisement.objects.get(id=advertisement_id)
            new_rev = Review(advertisement=advertisement, user=request.user, rating=request.POST["rating"], content=request.POST["content"] )
            new_rev.save()
        return redirect ("advertisements:advertisement_details_view",advertisement_id=advertisement.id)
    except Exception as e:
        return redirect('main:not_authorized')