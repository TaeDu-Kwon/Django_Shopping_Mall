from django.urls import path

from . import views

app_name = "shopping_mall"

urlpatterns = [
    path("", views.index, name = "index"),
]