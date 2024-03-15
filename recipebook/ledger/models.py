from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredients', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        'Profile',
        on_delete = models.CASCADE,
        related_name = 'users',
        default = None,
        null = True
    )

    created_on = models.DateTimeField(auto_now_add=True, null = True)
    update_on = models.DateTimeField(auto_now=True)

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name
