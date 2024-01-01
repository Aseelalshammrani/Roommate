from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path("contact_us/", views.contact_us_view , name="contact_us_view"),
    path('filter/', views.advertisement_filter_view, name="advertisement_filter_view"),
    path('not/found',views.not_found,name='not_found'),
    path('not/authorized',views.not_authorized,name='not_authorized'),
]
