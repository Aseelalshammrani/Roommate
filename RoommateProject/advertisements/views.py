from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Advertisement 

# Create your views here.

#Add a new advertisement
def add_advertisement_view(request:HttpRequest):
    if request.method == "POST":
        advertisement = Advertisement(
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
        city=request.POST['city']
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
        return redirect("advertisements:browse_advertisements_view")
    return render (request,'advertisements/add_advertisement.html',{'types_of_gender':Advertisement.types_of_gender,'types_of_residential':Advertisement.types_of_residential,'types_of_duration':Advertisement.types_of_duration,'cities':Advertisement.cities})

def browse_advertisements_view(request:HttpRequest):
    advertisements=Advertisement.objects.all()
    return render(request,'advertisements/browse_advertisements.html',{'advertisements':advertisements})


def advertisement_details_view(request:HttpRequest,advertisement_id):
    advertisement=Advertisement.objects.get(id=advertisement_id)
    return render(request,"advertisements/advertisement_details.html",{'advertisement':advertisement})


#Update advertisement
def update_advertisement_view(request:HttpRequest, advertisement_id):
    advertisement = Advertisement.objects.get(id=advertisement_id)
    if request.method == "POST":
        advertisement.title = request.POST["title"]
        advertisement.image = request.FILES["image"]
        advertisement.type_of_duration = request.POST["type_of_duration"]
        advertisement.duration_residence = request.POST["duration_residence"]
        advertisement.advertisement_date = request.POST["advertisement_date"]
        advertisement.type_of_residential = request.POST["type_of_residential"]
        advertisement.longitude = request.POST["longitude"]
        advertisement.latitiiude = request.POST["latitiiude"]
        advertisement.space = request.POST["space"]
        advertisement.price = request.POST["price"]
        advertisement.number_of_people = request.POST["number_of_people"]
        advertisement.features = request.POST["features"]
        advertisement.animal_allowed = request.POST["animal_allowed"]
        advertisement.min_age = request.POST["min_age"]
        advertisement.max_age = request.POST["max_age"]
        advertisement.gender = request.POST["gender"]
        advertisement.smoke_allowed = request.POST["smoke_allowed"]
        advertisement.advertisement_status = request.POST["advertisement_status"]
        advertisement.note = request.POST["note"]
        advertisement.rooms_number = request.POST["rooms_number"]
        advertisement.bathroom = request.POST["bathroom"]
        advertisement.has_kitchen = request.POST["has_kitchen"]
        advertisement.approved_status = request.POST["approved_status"]
        advertisement.save()
        return redirect("advertisements/advertisement_details_view", advertisement_id=advertisement.id)
    return render(request,"advertisements/update_advertisement_view", {"advertisement": advertisement})





    




