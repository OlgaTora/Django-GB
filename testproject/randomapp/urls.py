from django.urls import path
from . import views
from .views import choice_form

urlpatterns = [
    path('', views.index, name='index_random'),
    path('cube/<int:rolls>/', views.get_cube, name='cube'),
    path('number/<int:rolls>/', views.get_number, name='number'),
    path('h_or_t/<int:rolls>/', views.get_heads, name='heads_or_tails_v1'),
    path('heads_or_tails/', views.get_tails, name='heads_or_tails_v2'),
    path('choice_form/', choice_form, name='choice_form')
]
