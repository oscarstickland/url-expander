from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def redirect_view(request):
    return HttpResponse("Hello")
