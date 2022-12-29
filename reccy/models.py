from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Amount(models.Model):
    amount = models.DecimalField()
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.CharField(max_length=200)
