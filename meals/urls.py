from django.urls import path
from . import views

app_name='meals'

urlpatterns = [
    path('', views.meals_list, name="meals_list"),
    path('<slug:slug>', views.meals_details, name="meals_details"),
]
