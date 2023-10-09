import logging

from django import http
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import AddAuthorForm, AddArticleForm, AddCommentForm
from blog.models import Author, Article, Comment

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'blog/index_blog.html')


def author_read(request):
    authors = Author.objects.all()
    # return HttpResponse(authors)
    return render(
        request,
        'blog/authors.html',
        {'authors': authors}
    )


def article_read(request):
    articles = Article.objects.all()
    title = f'by all authors'
    # return HttpResponse(article)
    return render(
        request,
        'blog/articles.html',
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
            author = Author(name=name, surname=surname, mail=mail, birthday=birthday, biography=biography)
            author.save()
            logger.info(f'Add new author {name=}, {surname=}')
            message = 'Successfully operation'
    else:
        form = AddAuthorForm()
    return render(request,
                  'blog/add_new.html',
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
            article = Article(title=title, content=content, publish_date=publish_date, category=category, author=author)
            article.save()
            logger.info(f'Add new article {author=}, {title=}')
            message = 'Successfully operation'
    else:
        form = AddArticleForm()
    return render(request,
                  'blog/add_new.html',
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
        'blog/articles.html',
        {'articles': articles, 'title': title})


def article_content(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.views += 1
    article.save()
    comments = Comment.objects.filter(article=article).order_by('added_date')
    message = 'Add new comment'

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = Comment(article=article,
                              author=form.cleaned_data['author'],
                              comment_text=form.cleaned_data['comment_text'])
            comment.save()
            logger.info(f'Add new comment {comment.author=}, {comment.article=}')
            return http.HttpResponseRedirect('')
    else:
        form = AddCommentForm()
        return render(request,
                      'blog/article.html',
                      {'article': article, 'comments': comments, 'form': form, 'message': message})
