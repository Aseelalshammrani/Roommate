from django.db import models
from django.contrib.auth.models import User
from advertisements.models import Advertisement
from django_countries.fields import CountryField
# Create your models here.




class Profile(models.Model):

    genders = models.TextChoices("genders" , ["male","fmmale"])
    languages = models.TextChoices ("languages" , ["einglish","arabic"])
 

    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    personal_image = models.ImageField(upload_to="images/", default="images/ge.jpg")
    phone_number = models.CharField(max_length=64)
    gender = models.CharField( max_length=64, choices=genders.choices , default=genders.choices)
    age = models.IntegerField()
    about= models.TextField()
    language = models.CharField( max_length=64, choices=languages.choices , default=languages.choices )
    nationality = CountryField()

    def __str__(self):
        return f"{self.user.first_name} profile"



class Favorite(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)



class Validation(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    national_id = models.CharField(max_length=64)  
    id_image = models.ImageField(upload_to="images/")
    validated = models.BooleanField(default=False)






    
