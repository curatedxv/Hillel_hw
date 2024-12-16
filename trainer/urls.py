from django.urls import path

from . import views

urlpatterns = [
    #path('', views.user_page,  name='user_page'),
    #path('/<user_id>', views.specific_user, name='spec_user'),
    path('', views.trainer_page, name='trainer_page'),
    path('<trainer_id>',  views.specific_trainer, name='spec_trainer'),
    path('<trainer_id>/<service_id>', views.time_trainer, name='time_trainer')
]