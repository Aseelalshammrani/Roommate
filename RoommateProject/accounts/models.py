from django.db import models
from django.contrib.auth.models import User
from advertisements.models import Advertisement

# Create your models here.

class Profile(models.Model):
    genders = models.TextChoices("genders" , ["Male","Female"])
    languages = models.TextChoices ("languages" , ["English","Arabic"])
    nationalities= models.TextChoices("nationalities", ["Saudi","Non-Saudi"])
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    personal_image = models.ImageField(upload_to="images/", default="images/ge.jpg")
    phone_number = models.CharField(max_length=64)
    gender = models.CharField( max_length=64, choices=genders.choices)
    age = models.IntegerField()
    about= models.TextField()
    language = models.CharField( max_length=64, choices=languages.choices)
    nationality = models.CharField( max_length=64 ,choices= nationalities.choices)

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





    
