import random
import datetime
from django.core.management.base import BaseCommand
from blog.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Generate fake authors and articles."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Fake DB')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                name=f'Name{i}',
                surname=f'Surname{i}',
                mail=f'mail{i}@mail.ru',
                birthday=datetime.date.today() - datetime.timedelta(weeks=random.randint(100, 4000)),
                biography='Bla-bla-bla'
            )
            author.save()
            for j in range(1, count + 1):
                article = Article(
                    title=f'Title{j}',
                    content=f'Text from {author.name}'
                            f' #{j} is bla bla bla many long text',
                    author=author,
                    publish_date=datetime.date.today() - datetime.timedelta(days=random.randint(1, 365)),
                    is_published=random.choice([True, False]),
                    category=random.choice(['category1', 'category2']))
                article.save()
                for k in range(1, count + 1):
                    comment = Comment(
                        author=random.choice(Author.objects.all()),
                        article=article,
                        comment_text=f'Comments from {author}',
                        added_date=datetime.date.today() - datetime.timedelta(days=random.randint(1, 365)))
                    comment.save()
