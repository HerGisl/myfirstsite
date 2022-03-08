from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/dad/
    # http://localhost:8000/hermann/
    path('', views.index, name="person-index"),

]