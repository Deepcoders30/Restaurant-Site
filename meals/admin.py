from unicodedata import category
from django.contrib import admin
from .models import Meals
from .models import Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields='__all__'
    list_display=['name', 'preparation_time', 'people', 'price']
    search_fields=['name', 'description']
    list_filter=['category', 'people']

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)