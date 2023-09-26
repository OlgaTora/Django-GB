from django.urls import path
from . import views


urlpatterns = [
    path('cube/<int:rolls>/', views.get_cube, name='cube'),
    path('number/<int:rolls>/', views.get_number, name='number'),
    path('h_or_t/<int:rolls>/', views.get_heads, name='heads_or_tails_v1'),
    path('heads_or_tails/', views.get_tails, name='heads_or_tails_v2'),
]
