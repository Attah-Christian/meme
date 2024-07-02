from django.urls import path
from meme import views


urlpatterns = [
   path('', views.home, name='home'),
]

