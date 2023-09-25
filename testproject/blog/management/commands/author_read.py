from django.core.management.base import BaseCommand
from blog.models import Author


class Command(BaseCommand):
    help = "Get author by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        author = Author.objects.filter(pk=pk).first()
        self.stdout.write(f'Author: {author}')
