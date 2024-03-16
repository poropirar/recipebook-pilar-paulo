from django.urls import path
from .views import recipelist, recipe

urlpatterns = [
    path('recipes/list', recipelist, name='index'),
    path("recipe/<int:pk>/", recipe, name='recipe'),
]


app_name = "ledger"