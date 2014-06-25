# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from shopping.models import Recipe, RecipeElement, Ingredient, RecipeElementForm, ShoppingList
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from shopping.utils.decorators import user_owns_recipe, user_owns_shopping_list

class RecipeMixin(object):
    model = Recipe
    fields = ['name', 'servings', 'comment']
    success_url = reverse_lazy('shopping:recipe_list')
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Recipe', 'menu_category': 'recipe'})
        return kwargs

class ShoppingListMixin(object):
    model = ShoppingList
    fields = ['name', 'recipes']
    success_url = reverse_lazy('shopping:list_list')
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Shopping List', 'menu_category': 'shoppinglist'})
        return kwargs

class IngredientMixin(object):
    model = Ingredient
    success_url = reverse_lazy('shopping:ingredient_list')
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Ingredient', 'menu_category': 'ingredient'})
        return kwargs

def home(request):
    return render(request, 'shopping/home.html')

@login_required()
def recipe_list(request):
    latest_recipe_list = Recipe.objects.filter(owners__in=[request.user.id]).order_by('-creation_date')
    context = {'latest_recipe_list': latest_recipe_list, 'menu_category': 'recipe'}
    return render(request, 'shopping/recipe_list.html', context)

@login_required()
def shopping_list(request):
    latest_shopping_list = ShoppingList.objects.filter(owners__in=[request.user.id]).order_by('-creation_date')
    context = {'latest_shopping_list': latest_shopping_list, 'menu_category': 'shoppinglist'}
    return render(request, 'shopping/shopping_list.html', context)

@login_required()
def ingredient_list(request):
    latest_ingredient_list = Ingredient.objects.order_by('-creation_date')
    context = {'latest_ingredient_list': latest_ingredient_list, 'menu_category': 'ingredient'}
    return render(request, 'shopping/ingredient_list.html', context)

class RecipeCreate(RecipeMixin, CreateView):
    def form_valid(self, form):
        return_value = super(RecipeCreate, self).form_valid(form)
        form.instance.owners = [self.request.user]
        return return_value

class RecipeUpdate(RecipeMixin, UpdateView):
    pass

class RecipeDelete(RecipeMixin, DeleteView):
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(RecipeDelete, self).get_object()
        if self.request.user not in obj.owners.all():
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owners.all() == [request.user]:
            self.object.delete()
        else:
            self.object.owners.remove(request.user)
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ShoppingListCreate(ShoppingListMixin, CreateView):
    def form_valid(self, form):
        return_value = super(ShoppingListCreate, self).form_valid(form)
        form.instance.owners = [self.request.user]
        return return_value

class ShoppingListUpdate(ShoppingListMixin, UpdateView):
    pass

class ShoppingListDelete(ShoppingListMixin, DeleteView):
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ShoppingListDelete, self).get_object()
        if self.request.user not in obj.owners.all():
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owners.all() == [request.user]:
            self.object.delete()
        else:
            self.object.owners.remove(request.user)
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class IngredientCreate(IngredientMixin, CreateView):
    pass

class IngredientUpdate(IngredientMixin, UpdateView):
    pass

class IngredientDelete(IngredientMixin, DeleteView):
    pass

@user_owns_recipe()
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeElementForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        data = {'recipe': recipe.id}
        form = RecipeElementForm(initial=data)
        
    return render(request, 'shopping/recipe_detail.html', 
                  {'recipe': recipe, 
                   'elements': RecipeElement.objects.filter(recipe=recipe), 
                   'form': form}
                  )

@user_owns_shopping_list()
def shoppinglist_detail(request, list_id):
    shoppinglist = get_object_or_404(ShoppingList, pk=list_id)
    if request.method == 'POST':
        form = RecipeElementForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        data = {'shoppinglist': shoppinglist.id}
        form = RecipeElementForm(initial=data)

    elements = RecipeElement.objects.filter(recipe__in=shoppinglist.recipes.all())
    
    ingredients = set(map(lambda x:x.ingredient, elements))
    new_elements = []
    for ingredient in ingredients:
        gna = [y  for y in elements if y.ingredient==ingredient]
        details = [y.details()  for y in gna]
        new_elements.append([gna[0].ingredient.category.name, gna[0].ingredient.name, '+'.join(details)])
    
    return render(request, 'shopping/shoppinglist_detail.html', 
                  {'shoppinglist': shoppinglist, 
                   'elements': new_elements, 
                   'form': form}
                  )

@user_owns_recipe()
def remove_element(request, recipe_id, element_id):
    element = get_object_or_404(RecipeElement, pk=element_id)
    element.delete()
    return HttpResponseRedirect(reverse('shopping:recipe_detail', args=(recipe_id,)))
