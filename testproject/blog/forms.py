import datetime
from django import forms
from blog import models


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    mail = forms.EmailField()
    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'date'}))
    biography = forms.CharField()


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField()
    publish_date = forms.DateField(initial=datetime.date.today,
                                   widget=forms.DateInput(attrs={'class': 'date'}))
    category = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=models.Author.objects.all(), empty_label='Choose author')


class AddCommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=models.Author.objects.all(), empty_label='Choose your name')
    article = forms.ModelChoiceField(queryset=models.Article.objects.all(), empty_label='Choose article')
    comment_text = forms.CharField()
