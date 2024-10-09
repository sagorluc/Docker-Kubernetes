from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer): 
    class Meta:
        model  = Blog
        fields = ['id', 'title', 'author', 'image', 'paragraph', 'is_publish']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'image': 'Image',
            'paragraph': 'Paragraph',
            'is_publish': 'Publish or Draft'
        }