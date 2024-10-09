from django.shortcuts import render
from rest_framework import serializers, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated, NotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from blog.serializers import BlogSerializer
from blog.models import Blog

# Create your views here.
class BlogView(APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def handle_exception(self, exc):
        if isinstance(exc, NotAuthenticated):
            return Response({'error': 'Authentication is required to perform this action.'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().handle_exception(exc)
    
    def get(self, request, id=None):
        if id is not None:
            try:
                get_blog   = Blog.objects.get(id=id, is_publish='Publish')
                serializer = BlogSerializer(get_blog)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Blog.DoesNotExist:
                return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        
        pub_blog   = Blog.objects.filter(is_publish='Publish')
        if pub_blog:
            serializer = BlogSerializer(pub_blog, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Published blog not available'}, status=status.HTTP_404_NOT_FOUND)
            
    @csrf_exempt
    def post(self, request):
        data = request.data.copy()
        if request.method == 'POST':
            title      = data.get('title')
            author     = data.get('author')
            image      = data.get('image')
            paragraph  = data.get('paragraph')
            is_publish = data.get('is_publish')
            
            # Ensure 'image' is handled correctly
            if 'image' in request.FILES:
                data['image'] = request.FILES['image']
            
            if not title:
                return Response({'error': 'Title is not be empty.'}, status=status.HTTP_400_BAD_REQUEST)
            if not author:
                return Response({'error': 'Author is not be empty.'}, status=status.HTTP_400_BAD_REQUEST)
            if not image:
                return Response({'error': 'Image is not be empty.'}, status=status.HTTP_400_BAD_REQUEST)
            if not paragraph:
                return Response({'error': 'Paragraph is not be empty.'}, status=status.HTTP_400_BAD_REQUEST)
            if not is_publish:
                return Response({'error': 'Publish or draft is not be empty.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # if 'image' not in request.FILES:
            #     return Response({'error': 'Image file is required.'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = BlogSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)

                msg = {
                    'message': 'Blog created successfully.',
                    'data': serializer.data
                }
                return Response(msg, status=status.HTTP_201_CREATED)
            else:
                msg_error = serializer.errors
                return Response(msg_error, status=status.HTTP_400_BAD_REQUEST)
            
    @csrf_exempt
    def put(self, request, id=None):
        try:
            # Ensure the blog exists and belongs to the current user
            blog_user = Blog.objects.get(id=id, user=request.user)
        except Blog.DoesNotExist:
            raise NotFound({'error': 'Blog not found or you do not have permission to edit it.'})
        
        if request.method == 'PUT':
            data       = request.data
            serializer = BlogSerializer(blog_user, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                msg = {
                    'message': 'Blog updated successfully',
                    'data': serializer.data
                } 
                return Response(msg, status=status.HTTP_200_OK)
            else:
                msg = {
                    'message': 'Data is not valid',
                    'error': serializer.errors
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def patch(self, request, id=None):
        try:
            # Ensure the blog exists and belongs to the current user
            blog_user = Blog.objects.get(id=id, user=request.user)
        except Blog.DoesNotExist:
            raise NotFound({'error': 'Blog not found or you do not have permission to edit it.'})
        
        if request.method == 'PATCH':
            data       = request.data
            serializer = BlogSerializer(blog_user, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                msg = {
                    'message': 'Blog updated successfully',
                    'data': serializer.data
                } 
                return Response(msg, status=status.HTTP_200_OK)
            else:
                msg = {
                    'message': 'Data is not valid',
                    'error': serializer.errors
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)

                              
    @csrf_exempt
    def delete(self, request, id=None):
        try:
            get_blog = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            raise NotFound('Blog not found')
        
        get_blog.delete()
        msg = {
            'message': 'Blog delete successfully.'
        }
        return Response(msg, status=status.HTTP_200_OK)
            