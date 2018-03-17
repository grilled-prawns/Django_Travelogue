import django.contrib
from .models import Post


class PostModelAdmin(django.contrib.admin.ModelAdmin):
    list_display = ['title','created_date','publish_date','pk']
    list_display_links = ['created_date']
    list_editable = ['title']
    list_filter = ['title', 'created_date']
    search_fields = ['title', 'text']

    class Meta:
        model = Post


django.contrib.admin.site.register(Post, PostModelAdmin)

# Register your models here.
