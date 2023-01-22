"""Restaurant_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('home/', include('home.urls', namespace='home')),
    path('meals/', include('meals.urls', namespace='meals')),
    path('reservation/', include('reservation.urls', namespace='reservation')),
    path('blog/', include('Blog.urls', namespace='Blog')),
    path('aboutus/', include('aboutus.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('admin/', admin.site.urls),
    
    
]


urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header="Restoran Panel"
admin.site.site_title="Restoran App Admin"
admin.site.site_index_title="Welcome To Restoran Admin Panel"