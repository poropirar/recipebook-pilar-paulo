from django.db import models
<<<<<<< Updated upstream

# Create your models here.
=======
from django.urls import reverse
from django.contrib.auth.models import User

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_level = models.IntegerField()
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)
>>>>>>> Stashed changes
