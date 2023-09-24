from django.http import HttpResponse
from blog.models import Author


def author_read(request):
    authors = Author.objects.all()
    return HttpResponse(authors)