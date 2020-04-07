from django.urls import path
from . import views 


urlpatterns = [
    #paths de core
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name='category'),
]