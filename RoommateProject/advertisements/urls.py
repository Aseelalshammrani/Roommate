from django.urls import path
from . import views
app_name = "advertisements"
urlpatterns = [
    path('add/advertisement',views.add_advertisement_view,name='add_advertisement_view'),
    path('update/advertisement/<advertisement_id>/',views.update_advertisement_view,name='update_advertisement_view'),
    path('', views.advertisement_home_view, name='advertisement_home_view'),
    path('details/', views.advertisement_details_view , name='advertisement_details_view'),
    
]
