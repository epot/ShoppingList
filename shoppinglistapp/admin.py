from django.contrib import admin

from shoppinglistapp.models import Category
from shoppinglistapp.models import UnitMeasurement
from shoppinglistapp.models import Ingredient

# Register your models here.

admin.site.register(Category)
admin.site.register(UnitMeasurement)
admin.site.register(Ingredient)