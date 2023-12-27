from django.db import models
from django.contrib.auth.models import User



class Advertisement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    types_of_gender=models.TextChoices('types_of_gender',['Female','Male'])
    types_of_residential=models.TextChoices('types_of_residential',['Apartment','Room','House'])
    types_of_duration =models.TextChoices('types_of_duration',['Days','Weeks','Months'])
    cities=models.TextChoices('cities',['Riyadh'])
    approval_status=models.TextChoices('approval_status',['Pending','Approved','Denied'])
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images/")
    type_of_duration =models.CharField(max_length=500,choices=types_of_duration.choices)
    duration_residence=models.IntegerField()
    advertisement_date=models.DateTimeField(auto_now_add=True)
    type_of_residential=models.CharField(max_length=500,choices=types_of_residential.choices)
    longitude = models.DecimalField(max_digits=20, decimal_places=18)
    latitiiude=models.DecimalField(max_digits=20, decimal_places=18)
    space=models.FloatField()
    price=models.FloatField()
    number_of_people=models.IntegerField()
    animal_allowed=models.BooleanField(default=False)
    min_age=models.IntegerField()
    max_age=models.IntegerField()
    gender=models.CharField(max_length=500,choices=types_of_gender.choices)
    smoke_allowed=models.BooleanField(default=False)
    advertisement_status=models.BooleanField(default=True)
    note=models.TextField()
    rooms_number=models.IntegerField()
    bathroom=models.IntegerField()
    has_kitchen=models.BooleanField(default=False)
    approved_status=models.CharField(max_length=500,default='Pending',choices=approval_status.choices)
    city=models.CharField(max_length=500,choices=cities.choices)
    dishwasher=models.BooleanField(default=False)
    washing_machine=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title}"
    

class Advertisement_Image(models.Model):
    advertisement=models.ForeignKey(Advertisement,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/")


class Rent_Request(models.Model):
    order_status= models.TextChoices('order_status',['Pending','Approved','Denied','Finish'])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    order_status_choice = models.CharField(max_length=500,default='Pending',choices=order_status.choices)
    created_at = models.DateTimeField(auto_now_add=True)

