from django.contrib import admin

from shoppinglistapp.models import Category
from shoppinglistapp.models import UnitMeasurement
from shoppinglistapp.models import Ingredient
from shoppinglistapp.models import Recipe
from shoppinglistapp.models import RecipeElement

# Register your models here.

admin.site.register(Category)
admin.site.register(UnitMeasurement)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeElement)