from django.urls import path

from . import views

urlpatterns = [
    path('', views.booking_page, name='booking_page'),
    path('<int:booking_id>', views.specific_booking, name='specific_booking'),
    path('cancel', views.cancel_booking, name='cancel_booking'),
    path('accept', views.accept_booking, name='accept_booking')
]