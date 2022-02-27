from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/mom/
    # http://localhost:8000/johanna/
    path('', views.index, name="index"),
]