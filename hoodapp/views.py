from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('Welcome to our Neighbourhood')
    
    
    
def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})        
    
    
def login_user(request):
    form = LoginForm()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request, 'login.html',{'form':form})    
    
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    return render(request,'profile.html',{'profile':profile})
    
def edit_profile(request):
    profile = Profile(user=request.user)
    return render(request,'edit_profile.html',{'profile':profile})