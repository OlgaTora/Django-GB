from django.urls import path
from . import views


urlpatterns = [
    path('cube/', views.get_cube, name='cube'),
    path('number/', views.get_number, name='number'),
    path('heads_or_tails/', views.get_tails, name='heads_or_tails'),
]
