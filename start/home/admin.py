from django.contrib import admin

from home.models import Category, Post, Comment, Like


class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'time_create', 'image', 'moderation')
    list_display_links=('id', 'title')
    search_fields=('title', 'description')
    list_editable=('moderation',)
    list_filter=('moderation', 'time_create')


class СategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')
    search_fields=('name',)


# admin.site.register(User, UserAdmin)
admin.site.register(Category, СategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)

admin.site.site_header = 'Администрирование сайта #Start'


