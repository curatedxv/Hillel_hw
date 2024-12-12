from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def user_page(request):
    return HttpResponse('Hello')

def specific_user(request, user_id):
    return HttpResponse(f'Hello user')
def login_page(request):
    return HttpResponse('Login page')

def register_page(request):
    return HttpResponse('Register page')

def logout_page(request):
    return HttpResponse('Logout page')