from django.db import models
from django.contrib.auth.models import User
from .utils import getCountries, getState

# Create your models here.

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('seller', 'Seller')
    ]
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    passport = models.ImageField(upload_to='passports/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    country = models.CharField(max_length=30, choices=getCountries())
    
    
    
    