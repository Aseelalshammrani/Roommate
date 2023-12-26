from django.contrib import admin
from .models import Advertisement,Rent_Request
class AdvertisementAdmin(admin.ModelAdmin):
     list_filter =('approved_status',)

admin.site.register(Advertisement,AdvertisementAdmin)
admin.site.register(Rent_Request)
# Register your models here.
