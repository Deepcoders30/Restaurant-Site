from multiprocessing import context
from django.shortcuts import render
from .models import AboutUs, Why_Choose_Us, Chefs

# Create your views here.
def about_list(request):
    about=AboutUs.objects.last()
    why_choose_us=Why_Choose_Us.objects.all()
    chefs=Chefs.objects.all()


    context={
        'about': about,
        'why_choose_us': why_choose_us,
        'chefs':chefs
    }

    return render(request, 'about.html', context)