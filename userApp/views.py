from django.shortcuts import render
from django.views import generic
from .forms import SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.



class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("login")
    
 
@login_required   
def profileView(request):
    pass