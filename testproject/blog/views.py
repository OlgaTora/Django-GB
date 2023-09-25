from django.http import HttpResponse
from blog.models import Author, Article


def author_read(request):
    authors = Author.objects.all()
    return HttpResponse(authors)


def article_read(request):
    article = Article.objects.all()
    return HttpResponse(article)


def article_by_author(request):
    name = request.GET.get('name')
    author_id = Author.objects.filter(name=name).first()
    articles = Article.objects.filter(author_id=author_id).all()
    return HttpResponse(articles)
