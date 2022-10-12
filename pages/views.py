from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def homepage_view(request):
    return HttpResponse('hello world')

def room(request):
    return  HttpResponse("room")
