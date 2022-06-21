from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from. models import *
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    firstname= forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname= forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username','password1']
        
    def __init__(self,*args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'    
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user' ,)
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']        
        
        
        
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        fields = ['photo','name','content','location', 'health_cell','police_hotline'] 
        exclude = ['user']
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','content',]
        exclude = ['user']
        
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['business_name','email','description','neighborhood']
        exclude = ['user']