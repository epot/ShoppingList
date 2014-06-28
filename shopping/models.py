# -*- coding: utf-8 -*-

from datetime import datetime 

from django.db import models
from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Category')

class UnitMeasurement(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Unit measurement')
        verbose_name_plural = _('Units measurement')

class Ingredient(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    creation_date = models.DateTimeField(default=datetime.now(), editable=False)
    
    def __unicode__(self):
        return u"{} ({})".format(self.name, self.category)

    class Meta:
        verbose_name = _('Ingredient')

class Recipe(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    servings = models.IntegerField(verbose_name=_("Servings"))
    comment = models.TextField(max_length=4000, blank=True, null=True, verbose_name=_("Comment"))
    creation_date = models.DateTimeField(default=datetime.now(), editable=False)
    owners = models.ManyToManyField(User, verbose_name=_("Owners"))
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Recipe')

class IngredientForm(ModelForm):
    class Meta: 
        model = Ingredient

class ShoppingList(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    recipes = models.ManyToManyField(Recipe, verbose_name=_("Recipes"))
    creation_date = models.DateTimeField(default=datetime.now(), editable=False)
    owners = models.ManyToManyField(User, verbose_name=_("Owners"))

    class Meta:
        verbose_name = _('Shopping list')

class RecipeElement(models.Model):
    recipe = models.ForeignKey(Recipe, blank=True, null=True, verbose_name=_("Recipe"))
    shoppinglist = models.ForeignKey(ShoppingList, blank=True, null=True, verbose_name=_("Shopping list"))
    ingredient = models.ForeignKey(Ingredient, verbose_name=_("Ingredient"))
    unit_measurement = models.ForeignKey(UnitMeasurement, verbose_name=_("Unit measurement"))
    quantity = models.IntegerField(verbose_name=_("Quantity"))
    
    def __unicode__(self):
        return u"{} {} {}".format(self.quantity, self.unit_measurement, self.ingredient)

    def details(self):
        return u"{} {}".format(self.quantity, self.unit_measurement)

    class Meta:
        verbose_name = _('Recipe element')

class RecipeElementForm(ModelForm):
    class Meta: 
        model = RecipeElement
        widgets = {'recipe': HiddenInput(), 'shoppinglist': HiddenInput()}
       
