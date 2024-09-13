# from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# from django.contrib.auth.models import User


class UserCreateView(CreateView):
    # form passing
    form_class = UserCreationForm
    # model=User
    # fields=['email','username','password']
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('index_url')
