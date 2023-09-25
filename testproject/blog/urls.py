from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.author_read, name='authors'),
    path('articles/', views.article_read, name='articles'),
    path('articles_by_author/', views.article_by_author, name='articles_by_author'),
]
