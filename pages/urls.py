from django.urls import  path
#from  views import homepage_view
#from  views import  room

from . import views

urlpatterns = [

    path('', views.homepage_view, name = 'home'),
    path('room' , views.room),
    ]


