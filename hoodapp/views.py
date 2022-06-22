from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterForm,LoginForm,HoodForm,PostForm,BusinessForm,ProfileForm,UpdateForm
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    post= Post.objects.all()
    neighborhood = NeighborHood.objects.all()
    return render(request,'index.html',{'neighborhood':neighborhood,'post':post})
    
    
    
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
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        form = UpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and form.is_valid():
            form.save()
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        form = UpdateForm(instance=request.user.profile)
    return render(request,'edit_profile.html',{'form':form})
    
    
    
def hood(request):
    form = HoodForm()
    
    if request.method == 'POST':
        form =  HoodForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'hood.html',{'form':form}) 
    
    
def join_hood(request, hood_id):
    neighborhood = get_object_or_404(NeighborHood, id=hood_id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('index')
    
def leave_hood(request, hood_id):
    neighborhood = get_object_or_404(NeighborHood, id=hood_id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('index')    
    
def post(request,hood_id):
    neighborhood = NeighborHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighborhood = neighborhood
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        current_user = request.user
        neighborhood = NeighborHood.objects.get(id=hood_id)
        users = Profile.objects.filter(neighborhood=neighborhood)
        post = Post.objects.filter(neighborhood=neighborhood)
    return render(request, 'post.html', {'form':form, 'form': form, 'users':users,'current_user':current_user, 'neighborhood':neighborhood,'post':post})
    
    
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        
        form=BusinessForm(request.POST,request.FILES)

        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
            business.hood= hood
            business.save()
        return redirect('login')
    else:
        form=BusinessForm()
    return render (request,'business.html', {'form': form, 'profile': profile})