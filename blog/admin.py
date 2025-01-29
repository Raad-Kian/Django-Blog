
from django.contrib import admin
from .models import Post, Comment

# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'category', 'release_date', 'created_at')
    list_filter = ('category', 'release_date')
    search_fields = ('title', 'creator', 'genre')
    date_hierarchy = 'release_date'
    ordering = ('-created_at',)

# Register the Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__username', 'post__title')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)