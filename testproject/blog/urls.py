from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.author_read, name='authors'),
]
