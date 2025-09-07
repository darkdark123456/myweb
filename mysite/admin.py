from django.contrib import admin
from mysite.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "slug", "pub_date")
