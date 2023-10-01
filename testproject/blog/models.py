from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.EmailField()
    birthday = models.DateField()
    biography = models.TextField()

    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField()
    category = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.publish_date} {self.title} {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.TextField()
    added_date = models.DateField()
    update_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_text}'
