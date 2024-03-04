from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredients', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='ingredients',
        default=1
        )
    
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='recipes',
        default=1
        )


