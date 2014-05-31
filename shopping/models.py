from datetime import datetime 

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class UnitMeasurement(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "{} ({})".format(self.name, self.category)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=datetime.now())
    
    def __unicode__(self):
        return self.name

class RecipeElement(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    unit_measurement = models.ForeignKey(UnitMeasurement)
    quantity = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "{} {} {}".format(self.quantity, self.unit_measurement, self.ingredient)
