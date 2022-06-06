from django.contrib import admin
from blog.models import Blog, Comment_blog
from modeltranslation.admin import TranslationAdmin

class BlogAdmin(TranslationAdmin):
    list_display = ['title',  'image',  'status', 'create_at',]


class Comment_blogAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'comment', 'status',]
    list_filter = ['status']
    readonly_fields = ('name', 'surname', 'phone', 'comment', 'ip',  'blog',)



admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment_blog, Comment_blogAdmin)