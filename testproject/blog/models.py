from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.EmailField()
    birthday = models.DateField()
    biography = models.TextField()

    def full_name(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField()
    category = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

