from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [

     path("register/", views.register_user_view, name="register_user_view"),
     path("login/", views.login_user_view, name="login_user_view"),
     path("logout/", views.logout_user_view, name="logout_user_view"),
     path("profile/<int:user_id>/", views.user_profile, name="user_profile"),
     path("update/", views.update_user_view, name="update_user_view"),
     path('<advertisement_id>/add/', views.add_favorite_view, name="add_favorite_view"),
     path('my/favorite/', views.my_favorite_view, name="my_favorite_view"),
     path('validation_user/',views.validation_user_view, name="validation_user_view"),
     path('success_page/',views.success_page,name='success_page'),
     path('advertisement_user/',views.advertisement_user,name="advertisement_user"),
     path('vali/',views.admin_validation_requests, name='admin_validation_requests'),
     path('validate/<validation_id>/', views.approve_validation , name="approve_validation"),
     path('confirmation/',views.confirmation_view, name="confirmation_view"),
     path('validation_detail/<user_id>/', views.validate_detail_view, name="validate_detail_view"),
     path('my/requsets/<user_id>/',views.my_requset,name='my_requset'),
     path('send/rent/request/<advertisement_id>/',views.send_rent_request,name='send_rent_request'),
     path('my/roommate/<user_id>/',views.receive_rent_request,name='receive_rent_request'),
     path('accept/rent/request/<rent_request_id>/',views.accept_rent_request,name='accept_rent_request'),
     path('cancel/rent/request/<rent_request_id>/',views.cancel_rent_request,name='cancel_rent_request'),

]
