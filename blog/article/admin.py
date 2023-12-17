from django.contrib import admin

from .models import Article
# Register your models here.

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date","content"]

    list_display_links = ["title","author","created_date","content"]

    search_fields = ["title","author","created_date","content"]

    list_filter = ["title","author","created_date","content"]
    class Meta:
        model= Article

