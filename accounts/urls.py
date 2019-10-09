
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('profile/', views.profile, name='profile')
]
