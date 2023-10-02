from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_blog'),
    path('authors/', views.author_read, name='authors'),
    path('authors/add_new_author/', views.add_author_form, name='add_new_author'),
    path('articles/', views.article_read, name='articles'),
    path('articles/add_new_article/', views.add_article_form, name='add_new_article'),
    path('articles/author/<str:name>/', views.article_by_author, name='articles_by_author'),
    path('article/<int:pk>/', views.article_content, name='article_content'),
    path('articles/add_new_comment/', views.add_comment_form, name='add_new_comment'),

]
