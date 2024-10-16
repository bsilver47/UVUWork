from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("silver", views.silver, name="silver"),
    path("<str:name>", views.greet, name="greet")
]
