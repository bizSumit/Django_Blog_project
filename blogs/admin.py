from django.contrib import admin
from .models import Blog, Author


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 2
    fields = ['title', 'date']
    readonly_fields = [field.name for field in Blog._meta.get_fields()]
    

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')
    inlines = [BlogInline,]


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author', 'date')
    autocomplete_fields = ['author',]
    search_fields = ['title', 'author__name','author__email',]
    search_help_text = 'Search blog by title or author'
    fields = ('title', 'author', 'blog_text')
    readonly_fields = ['title',]
    


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
