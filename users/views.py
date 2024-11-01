from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  User
# Create your views here.
def index(request):
    return HttpResponse("hello world")



def view_user(request):
    #devo serializzare il modello per stamparlo
    return HttpResponse("serializza il modello")