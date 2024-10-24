from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#create a list view:
def posts_home():
    return HttpResponse("<h1>Hello</h1>")