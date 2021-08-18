from django.urls import path
from . import views



urlpatterns = [
   path('', views.Home, name='home'),
   path('blog', views.Blog, name='blog'),
   path('contact', views.Contact, name='contact'),
   path('rendez-vous', views.RendezVous, name='rendez-vous'),
]
