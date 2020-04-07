from django.urls import path
from . import views as views1
from services import views as services_views

urlpatterns = [
    path('', services_views.services, name="services"),
   
]