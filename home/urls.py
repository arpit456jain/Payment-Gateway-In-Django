from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.loginuser, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('makePayment/', views.makePayment, name='makePayment'),
     path('success/' ,views.success , name='success'),
    
]
