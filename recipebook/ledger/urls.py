from django.urls import path

from .views import recipelist,recipe1,recipe2

urlpatterns = [
path('recipes/list', recipelist, name='index'),
path('recipe/1', recipe1, name='index'),
path('recipe/2', recipe2, name='index'),

]


app_name = "ledger"