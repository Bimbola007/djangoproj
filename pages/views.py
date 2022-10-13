from django.shortcuts import render
#from  django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class Homepage_View(TemplateView):
    template_name = 'homepage_view.html'

class Room(TemplateView):
    template_name = 'room.html'
