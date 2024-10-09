from django.db import models
from django.contrib.auth.models import User
from accounts.constants import PUBLISH

# Create your models here.
class Blog(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')
    title      = models.CharField(max_length=200, verbose_name='Title', blank=True, null=True)
    author     = models.CharField(max_length=150, verbose_name='Author', blank=True, null=True)
    image      = models.ImageField(upload_to='photo/', default='photo/img.png', verbose_name='Image', blank=True, null=True)
    paragraph  = models.TextField(verbose_name='Paragraph')
    is_publish = models.CharField(max_length=100, verbose_name='Publish or Draft', choices=PUBLISH, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name        = 'Blog'
        verbose_name_plural = 'Blogs'
        
    def __str__(self) -> str:
        return self.title
