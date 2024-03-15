from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredient(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredient]

admin.site.register(Recipe, RecipeAdmin)