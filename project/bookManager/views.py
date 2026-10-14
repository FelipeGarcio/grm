from django.shortcuts import render
from views import home
from django.http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse(content=":)")