from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('booking/',views.booking,name="booking"),
    path('eventes/',views.eventes,name="eventes"),
    
    
    
]