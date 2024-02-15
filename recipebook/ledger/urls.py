from django.urls import path

from .views import recipelist

urlpatterns = [
path('recipes/list', recipelist, name='index'),
]


app_name = "ledger"