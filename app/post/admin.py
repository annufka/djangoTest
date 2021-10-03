from django.contrib import admin

from app.post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "creation_date")


admin.site.register(Post, PostAdmin)
