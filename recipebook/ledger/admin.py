from django.contrib import admin
from .models import Recipe, RecipeIngredient
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipeIngredient(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredient]

admin.site.register(Recipe, RecipeAdmin)