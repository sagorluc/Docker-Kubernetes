from django.urls import path, include
from blog.views import (
    BlogView,
    )
   
   
urlpatterns = [
    # Blog
    path('blog_list/', BlogView.as_view(), name='blog_list'),
    path('blog_list/<int:id>/', BlogView.as_view(), name='blog_single'),
    path('create_blog/', BlogView.as_view(), name='create_blog'),
    path('compelete_update/<int:id>/', BlogView.as_view(), name='complete_update'),
    path('partial_update/<int:id>/', BlogView.as_view(), name='partial_update'),
    path('delete/<int:id>/', BlogView.as_view(), name='delete_blog'),
]
