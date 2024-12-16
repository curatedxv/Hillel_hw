from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def booking_page(request):
    return HttpResponse("Booking page")

def specific_booking(request, booking_id):
    return HttpResponse("Specific booking")

def cancel_booking(request):
    return HttpResponse("Cancel booking")

def accept_booking(request):
    return HttpResponse("Accept booking")