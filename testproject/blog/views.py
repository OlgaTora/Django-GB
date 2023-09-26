from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Author, Article


def author_read(request):
    authors = Author.objects.all()
    return HttpResponse(authors)


def article_read(request):
    article = Article.objects.all()
    return HttpResponse(article)


# def article_by_author(request):
#     author = request.GET.get('author')
#     author_id = Author.objects.filter(name=author).first()
#     articles = Article.objects.filter(author_id=author_id).all()
#     return HttpResponse(articles)

def article_by_author(request, name):
    author = get_object_or_404(Author, name=name)
    articles = Article.objects.filter(author=author)
    return render(
        request,
        'articles.html',
        {'author': author, 'articles': articles})


def article_content(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request,
                  'article.html',
                  {'article': article})
