from django.urls import path
from . import  views

urlpatterns=[
    path('',views.home),
    path('index/',views.index),
    path('register/',views.register),
    path('signin/',views.signin),
    path('contact/',views.contact),
    path('about/',views.about),
    path('events/',views.events),
    path('details/',views.details),
    path('myprofile/',views.myprofile),
]
