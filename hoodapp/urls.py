from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('register', views.register,name = 'register'),
    path('login/', views.login,name = 'login'),
    path('profile',views.profile,name ='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('hood',views.hood,name ='hood'),
    path('join_hood/<hood_id>',views.join_hood,name='join'),
    path('leave_hood/<hood_id>',views.leave_hood,name='leave'),
    path('post',views.post,name='post'),
    path('business',views.create_business,name='business'),
]    