from turtle import title
from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.



class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField("image",null=True)
    content = models.TextField(max_length=600, null=True)
    location = models.CharField(max_length=200,null=True)
    occupants_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    health_cell = models.IntegerField(null=True, blank=True)
    police_hotline = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
    def update_neighborhood(self):
        self.update()
    def update_occupants(self):
        self.update()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio= models.TextField()
    profile_photo = CloudinaryField('images')
    contact = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,null=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()




class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    content = models.TextField(blank=True, null=True)
    profile_photo = CloudinaryField("image",blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,null=True)
    class Meta:
        ordering = ['-pk']
        
    def __str__(self):
        return f'{self.title} Post'
    
    def delete_post(self):
        self.delete()
    

    def create_post(self):
        self.save()
        
    def update_post(self):
        self.update()
    
    
class Business(models.Model):
    business_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,null=True)
    
    def create_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
    def update_business(self):
        self.update()    
        
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)
    
    @classmethod
    def search_by_business_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business