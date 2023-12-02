from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(res):
    return HttpResponse('<h1>This is first app home page</h1>')