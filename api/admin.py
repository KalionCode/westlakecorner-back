from django.contrib import admin
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ('name',)
