from django.contrib.auth import authenticate, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def user_page(request):
    return HttpResponse('Hello')

def specific_user(request, user_id):
    return HttpResponse(f'Hello user')
def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful')
        else:
            render(request, 'login.html')
def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username=username, password=password,  email=email, first_name=first_name, last_name=last_name)
        user.save()
        return HttpResponse('Register successful')
    else:
        return render(request, 'register.html')
    #user = User.objects.create_user(username='john', password='12345678')
    #user.last_name = 'Lemon'
    #user.save()
    #return HttpResponse('Register page')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse('Logout successful')