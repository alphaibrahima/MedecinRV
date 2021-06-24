from django.urls import path
from . import views



urlpatterns = [
   path('', views.Home, name='home'),
   path('contact.html', views.Contact, name='contact'),
]
