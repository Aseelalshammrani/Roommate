from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('genders/', views.advertisements_genders_view, name="advertisements_genders_view"),
    path("female/", views.advertisements_female_gender_view, name="advertisements_female_gender_view"),
    path('male/', views.advertisements_male_gender_view, name='advertisements_male_gender_view'),
    path('less/cost/', views.cost_less_filter_view, name='cost_less_filter_view'),
    path('more/cost/',views.cost_more_filter_view, name='cost_more_filter_view'),
    path('cost/',views.cost_view, name="cost_view"),
    path('filter/', views.advertisement_filter_view, name="advertisement_filter_view")
    path('not/found',views.not_found,name='not_found'),
    path('not/authorized',views.not_authorized,name='not_authorized')
]
