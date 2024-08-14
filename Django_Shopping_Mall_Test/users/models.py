from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_CATEGORIES = [
        ("General_User","일반 유저"),
        ("Business_User","사업자 유저")
    ]

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    category = models.CharField(max_length = 30 , choices = USER_CATEGORIES)
    address = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.category}"
    

class Business_Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.company_name}"