from django.urls import path

from .views import RecipeDetailView,RecipeListView

urlpatterns = [
path('recipes/list', RecipeListView.as_view(), name='list'),
path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipes'),
]


app_name = "ledger"