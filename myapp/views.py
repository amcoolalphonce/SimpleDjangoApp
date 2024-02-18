from django.shortcuts import render, redirect  #redirect for authentication
#authentication imports 
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def index(request):
        return render(request, 'myapp/index.html')
 
def about(request):
        return render(request, 'myapp/about.html')

#authentivation views
def login_user(request):
        return render(request,'myapp/login.html' )