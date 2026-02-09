from django.contrib import admin
from .models import UserProfile

# Register your models here.
admin.site.site_header = "Ojaoba Admin"
admin.site.site_title = "Ojaoba Admin Portal"
admin.site.register(UserProfile)