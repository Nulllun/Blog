from django.contrib import admin

from .models import Post, Comment, Profile


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title','author']}),
        (None,  {'fields': ['body']}),

    ]
    inlines = [CommentInline]
    list_display = ('title', 'author', 'create_date')


admin.site.register(Post,PostAdmin)
admin.site.register(Profile)
