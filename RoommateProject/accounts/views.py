from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from advertisements.models import Advertisement,Rent_Request
from .models import Favorite ,Profile ,Validation
from advertisements.models import Advertisement
from django.db import IntegrityError

# Create your views here.


def register_user_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
        
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()


            user_profile = Profile(user=user, personal_image=request.FILES["personal_image"], age=request.POST["age"])
            user_profile.save() 

            return redirect("accounts:login_user_view")
        
        except IntegrityError as e:
            msg = f"Please select another username {e}"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/register.html", {"msg" : msg})


def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user:
                login(request, user)
                return redirect("main:home_page")
            else:
                msg = "Please provide correct username and password"
        except Exception as e:
            msg = f"something went wrong {e}"
            
    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user_view(request: HttpRequest):
     if request.user.is_authenticated:
        logout(request) 
     return redirect("accounts:login_user_view")


def user_profile(request: HttpRequest, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        return render(request, 'main/not_found.html')
    return render(request, 'accounts/profile.html', {"user":user })


def update_user_view(request: HttpRequest):
    msg = None
 
    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                user : User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

            
                try:
                    profile : Profile = request.user.profile
                except Exception as e:
                    profile = Profile(user=user, age=request.POST["age"])
                    profile.save()

                profile.age = request.POST["age"]

                if 'personal_image' in request.FILES: profile.personal_image = request.FILES["personal_image"]
                profile.phone_number = request.POST["phone_number"]
                profile.gender = request.POST["gender"]
                profile.about = request.POST["about"]
                profile.language = request.POST["language"]
                profile.nationality = request.POST["nationality"]
                profile.save()

                return redirect("accounts:user_profile", user_id = request.user.id)

            else:
                return redirect("accounts:login_user_view")
        except IntegrityError as e:
            print(e)
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/update.html", {"msg" : msg,'languages':Profile.languages, "genders":Profile.genders,"nationalities":Profile.nationalities})



def add_favorite_view(request:HttpRequest, advertisement_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

    try:
        advertisement = Advertisement.objects.get(id=advertisement_id)
        user_favored = Favorite.objects.filter(user=request.user, advertisement=advertisement).first() 
        
        if not user_favored:
            new_favorite = Favorite(user=request.user, advertisement=advertisement)
            new_favorite.save()
        else:

            user_favored.delete()

        return redirect("advertisements:advertisement_details_view", advertisement_id=advertisement.id)
    except Exception as e:
        return redirect("main:home_page")


def my_favorite_view(request: HttpRequest):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'accounts/my_favorite.html', {"favorites" : favorites})

def delete_favorite(request: HttpRequest,advertisement_id):
    advertisement = Advertisement.objects.get(id=advertisement_id)
    favorite= Favorite.objects.filter(user=request.user,advertisement=advertisement)
    favorite.delete()
    return redirect('accounts:my_favorite_view')

def validation_user_view(request: HttpRequest):
    msg =None
    pre_validation = None
    
    if request.method=="POST":

        try:
            pre_validation = Validation.objects.filter(user=request.user).first()
            if not pre_validation:
                validation = Validation (
                user =request.user, 
                national_id =request.POST["national_id"],
                id_image= request.FILES["id_image"],
                )
                validation.save()
                return redirect( "accounts:success_page")
            else:
                msg = "You have a previous application"
        except IntegrityError as e:
            msg = f"something went wrong {e}"
    return render(request, 'accounts/validation.html', {"msg":msg})


def success_page(request: HttpRequest):
    return render(request, 'accounts/success_page.html')


def advertisement_user(request: HttpRequest):
    user = request.user  
    advertisements = user.advertisement_set.all() 
    context = {'advertisements': advertisements} 
    return render(request, 'accounts/advertisement_user.html', context)

def confirmation_view(request:HttpRequest):
    return render(request,'accounts/confirmation.html')

def admin_validation_requests(request: HttpRequest):
    validations = Validation.objects.filter(validated=False)
    return render(request, 'accounts/admin_page.html', {'validations': validations})

def approve_validation(request:HttpRequest, validation_id):
    msg= None
    if request.method == 'POST':
        try:
            validation = Validation.objects.get(id=validation_id)
            validation.validated = True
            validation.save()

            return redirect('accounts:confirmation_view')
        except Exception as e:
            msg = f"something went wrong {e}"
    return render(request, 'accounts/validation_detail.html', {'validation_id': validation_id ,"msg":msg})


def validate_detail_view(request:HttpRequest,user_id):
    msg=None
    validation=None
    try:
        user = User.objects.get(id=user_id)
        validation = Validation.objects.get(user=user)
    except Exception as e:
        print(e)
        msg=f"something went wrong{e}"
    return render(request,'accounts/validation_detail.html', {"user":user, "validation":validation, "msg":msg})

def my_requset(request:HttpRequest,user_id):
    requsets=Rent_Request.objects.filter(user=user_id)
    return render(request,'accounts/rent_request.html',{'requsets':requsets})

def send_rent_request(request:HttpRequest, advertisement_id):
    msg= None
    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    try:
        advertisement = Advertisement.objects.get(id=advertisement_id)
        if request.user != advertisement.user:
            rent_request=Rent_Request.objects.filter(user=request.user,advertisement=advertisement).first()
            if not rent_request:
                new_rent_request = Rent_Request(user=request.user,advertisement=advertisement)
                new_rent_request.save()
        return redirect("advertisements:advertisement_details_view",  advertisement_id=advertisement.id)
    except Exception as e:
        return redirect("advertisements:advertisement_details_view",  advertisement_id=advertisement.id)
       
def receive_rent_request(request:HttpRequest,user_id):
    msg = None
    receive_rent_requests = None  # Use plural for clarity
    try:
        # Retrieve advertisements for the current user (request.user)
        advertisements = Advertisement.objects.filter(user=request.user)

        if advertisements:  # Check if any advertisements exist
            receive_rent_requests = Rent_Request.objects.filter(advertisement__in=advertisements)
        else:
            msg = "You don't have any advertisements yet."

    except Exception as e:
        msg = f"An error occurred while retrieving rent requests: {e}"
    return render(request,'accounts/my_roommate.html',{'receives':receive_rent_requests,"msg":msg, "order_status": Rent_Request.order_status})

def accept_rent_request(request, rent_request_id):
    try:
        rent_request = Rent_Request.objects.get(id=rent_request_id)
        if request.GET.get("order_status_choice") == "Approved":
            rent_request.order_status_choice= "Approved"
        elif request.GET.get("order_status_choice") == "Denied":
            rent_request.order_status_choice= "Denied"
        elif request.GET.get("order_status_choice") == "Finish":
            rent_request.order_status_choice= "Finish"
        elif request.GET.get("order_status_choice") == "Pending":
            rent_request.order_status_choice= "Pending"
        rent_request.save()
        return redirect('accounts:receive_rent_request',user_id=request.user)
    except Exception as e:
        return redirect('accounts:receive_rent_request',user_id=request.user)

def cancel_rent_request(request, rent_request_id):
    rent_request = Rent_Request.objects.get(id=rent_request_id)
    rent_request.delete()
    return redirect('accounts:my_requset',user_id=request.user.id)

def my_comments(request:HttpRequest):

    return render(request,'accounts/my_comments.html')
