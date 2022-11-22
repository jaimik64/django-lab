from django.urls import path  
from .views import profile,login_request 
  
  
urlpatterns = [  
    path('profile', profile, name = 'profile') , 
    path('login', login_request, name = 'login')  
]  