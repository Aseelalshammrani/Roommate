from django.urls import path
from . import views
app_name = "advertisements"
urlpatterns = [
    path('add/advertisement',views.add_advertisement,name='add_advertisement')
    
]
