from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render
class RecipeListView(ListView):
    model = Recipe
    template_name = 'listofrecipes.html'


    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe1.html'
