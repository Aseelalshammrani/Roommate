from django.contrib import admin
from .models import Advertisement,Rent_Request,Advertisement_Image
class AdvertisementAdmin(admin.ModelAdmin):
     list_filter =('approved_status',)

admin.site.register(Advertisement,AdvertisementAdmin)
admin.site.register(Rent_Request)
admin.site.register(Advertisement_Image)
# Register your models here.
