from django.urls import  path
from .views import Homepage_View, Room, AboutPage

urlpatterns = [

    path('', Homepage_View.as_view(), name= 'home'),
    path('room/' , Room.as_view() , name= 'room'),
    path('about/', AboutPage.as_view(), name= 'about'),
    ]


