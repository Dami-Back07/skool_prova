from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  User
# Create your views here.
def index(request):
    return HttpResponse("hello world")



def view_user(request):
    #devo serializzare il modello per stamparlo
    return HttpResponse("users")

def view_post(request):
    return HttpResponse("posts")

def user_detail(request , user_id : int):
    return HttpResponse(f"users/{user_id}")

def post_detail(request , post_id : int):
    return HttpResponse(f"posts/{post_id}")