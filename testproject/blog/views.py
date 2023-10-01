import logging

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import AddAuthorForm, AddArticleForm
from blog.models import Author, Article, Comment

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index_blog.html')


def author_read(request):
    authors = Author.objects.all()
    # return HttpResponse(authors)
    return render(
        request,
        'authors.html',
        {'authors': authors}
    )


def article_read(request):
    articles = Article.objects.all()
    title = f'by all authors'
    # return HttpResponse(article)
    return render(
        request,
        'articles.html',
        {'articles': articles, 'title': title})


def add_author_form(request):
    message = 'Please fill form to add new author'
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            mail = form.cleaned_data['mail']
            birthday = form.cleaned_data['birthday']
            biography = form.cleaned_data['biography']
            logger.info(f'Add new author {name=}, {surname=}')
            author = Author(name=name, surname=surname, mail=mail, birthday=birthday, biography=biography)
            author.save()
            message = 'Successfully operation'
    else:
        form = AddAuthorForm()
    return render(request,
                  'add_new.html',
                  {'form': form, 'message': message})


def add_article_form(request):
    message = 'Please fill form to add new article'
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            category = form.cleaned_data['category']
            author = form.cleaned_data['author']
            views = form.cleaned_data['views']
            is_published = form.cleaned_data['is_published']
            logger.info(f'Add new article {author=}, {title=}')
            article = Article(title=title, content=content, publish_date=publish_date, category=category, author=author,
                              views=views, is_published=is_published)
            article.save()
            message = 'Successfully operation'
    else:
        form = AddArticleForm()
    return render(request,
                  'add_new.html',
                  {'form': form, 'message': message})


# def article_by_author(request):
#     author = request.GET.get('author')
#     author_id = Author.objects.filter(name=author).first()
#     articles = Article.objects.filter(author_id=author_id).all()
#     return HttpResponse(articles)

def article_by_author(request, name):
    author = get_object_or_404(Author, name=name)
    articles = Article.objects.filter(author=author)
    title = f'by {author}'
    return render(
        request,
        'articles.html',
        {'articles': articles, 'title': title})


def article_content(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.views += 1
    article.save()
    comments = Comment.objects.filter(article=article).order_by('added_date')
    update = 'updated'
    return render(request,
                  'article.html',
                  {'article': article, 'comments': comments, 'update': update})
