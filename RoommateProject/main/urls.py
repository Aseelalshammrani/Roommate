from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('approve/', views.approve_accounts_view, name="approve_accounts_view")
]
