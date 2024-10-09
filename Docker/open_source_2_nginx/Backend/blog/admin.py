from django.contrib import admin
from blog.models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'title', 'image', 'is_publish']
    ordering      = ['-id']
    search_fields = ('title', 'author')
    list_filter   = ('is_publish', 'created_at')
    
admin.site.register(Blog, BlogAdmin)