from django.urls import path
from . import views 


urlpatterns = [
    #paths de core
    path('<int:page_id>/', views.page, name='page'),
]