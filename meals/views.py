from multiprocessing import context
from django.shortcuts import render
from .models import Meals, Category

def meals_list(request):
    meals_list = Meals.objects.all()
    categories=Category.objects.all()
    context={'meals_list':meals_list, 'categories':categories}

    return render(request, "Meals/list.html", context)

def meals_details(request, slug):
    meals_details=Meals.objects.get(slug=slug)

    context = {'meals_details':meals_details}

    return render(request, "Meals/detail.html", context)
