from django.contrib import admin
from .models import Author, Article, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'birthday']
    ordering = ['surname']
    list_filter = ['surname']
    readonly_fields = ['name']


@admin.action(description='Reset views')
def reset_views(modeladmin, request, queryset):
    queryset.update(views=0)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date', 'views', 'content']
    ordering = ['author', '-views']
    list_filter = ['author', 'publish_date']
    list_per_page = 5
    actions = [reset_views]
    readonly_fields = ['author', 'content']
    search_fields = ['title']
    search_help_text = 'search'
    fieldsets = [
        (
            'Info about of article',
            {
                'classes': ['wide'],
                'description': 'information',
                'fields': ['title', 'author'],
            },
        ),
        (
            'Content of article',
            {
                'classes': ['wide'],
                'description': 'content of article',
                'fields': ['content'],
            },
        ),
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'added_date']
    list_filter = ['author', 'article']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
