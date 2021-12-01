from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageViews(reguest):
    return HttpResponse('<h1>Hello World!</hi>')

