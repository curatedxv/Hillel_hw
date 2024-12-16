from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trainer_page(request):
    return HttpResponse('Trainer ')
def specific_trainer(request, trainer_id):
    return HttpResponse(f'Trainer {trainer_id}')
def time_trainer(request, trainer_id, service_id):
    return HttpResponse(f'Trainer {trainer_id} {service_id}')
