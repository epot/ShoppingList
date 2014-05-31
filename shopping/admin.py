from django.contrib import admin

from shopping.models import Category
from shopping.models import UnitMeasurement
from shopping.models import Ingredient
from shopping.models import Recipe
from shopping.models import RecipeElement

# Register your models here.

admin.site.register(Category)
admin.site.register(UnitMeasurement)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeElement)