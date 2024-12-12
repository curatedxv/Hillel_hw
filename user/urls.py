from django.urls import path

from Django.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.user_page,  name='user_page'),
    path('/<user_id>', views.specific_user, name='spec_user'),
]