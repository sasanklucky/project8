from django.urls import path 
from app2.views import *
app_name='aa'
urlpatterns=[
    path('pushpa/',pushpa,name='pushpa'),
    path('meghna/',meghna,name='meghna'),
]