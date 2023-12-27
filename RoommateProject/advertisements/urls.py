from django.urls import path
from . import views
app_name = "advertisements"
urlpatterns = [
    path('add/advertisement',views.add_advertisement_view,name='add_advertisement_view'),
    path('update/advertisement/<advertisement_id>/',views.update_advertisement_view,name='update_advertisement_view'),
    path('advertisement/details/<advertisement_id>/', views.advertisement_details_view, name='advertisement_details_view'),
    path('browse_advertisements', views.browse_advertisements_view , name='browse_advertisements_view'),
    path('delete/advertisement/<advertisement_id>/',views.delete_advertisement_view,name='delete_advertisement_view'),
    path('search/',views.search,name="search"),
]
