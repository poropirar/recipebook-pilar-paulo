from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Ingredient, Recipe, RecipeIngredient

def recipelist(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "listofrecipes.html", context)

@login_required
def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        "name": recipe.name,
        "author": recipe.author,
        "created_on": recipe.created_on,
        "updated_on": recipe.update_on,
        "ingredients": RecipeIngredient.objects.filter(recipe__name=recipe.name),
    }


    return render(request, "recipe1.html", context)

    # Create your views here.
