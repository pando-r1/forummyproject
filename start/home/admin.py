from django.contrib import admin

from home.models import Category, Post, Comment, Like

# admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)