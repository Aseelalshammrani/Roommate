from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [

     path("register/", views.register_user_view, name="register_user_view"),
     path("login/", views.login_user_view, name="login_user_view"),
     path("logout/", views.logout_user_view, name="logout_user_view"),
     path("profile/<int:user_id>/", views.user_profile, name="user_profile"),
     path("update/", views.update_user_view, name="update_user_view"),
     path('<advertisement_id>/add/', views.add_favorite, name="add_favorite"),
     path('favorite/', views.favorite, name="favorite"),
     path('validation_user/',views.validation_user_view, name="validation_user_view"),
     path('success_page/',views.success_page,name='success_page'),
     path('vali/',views.admin_validation_requests, name='admin_validation_requests'),
     path('validate/<validation_id>/', views.approve_validation , name="approve_validation"),
     path('confirmation/',views.confirmation_view, name="confirmation_view"),
     path('validation_detail/<user_id>/', views.validate_detail_view, name="validate_detail_view")
  
]
