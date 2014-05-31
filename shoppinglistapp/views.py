from django.shortcuts import render, get_object_or_404
from shoppinglistapp.models import Recipe, RecipeElement

# Create your views here.
def index(request):
    latest_recipe_list = Recipe.objects.order_by('-creation_date')[:5]
    print latest_recipe_list
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'shoppinglistapp/index.html', context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'shoppinglistapp/recipe_detail.html', {'recipe': recipe, 'elements': RecipeElement.objects.filter(recipe=recipe)})