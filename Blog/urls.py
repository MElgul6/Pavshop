from django.urls import path
from Blog.views import (
    BlogListView,
    BlogDetailView
)

urlpatterns = [
    # path('blog/<str:pk>/',blog, name = 'blogs'),
    path('blogs/<str:pk>/',BlogDetailView.as_view(), name = 'blog'),
    path('blogs/', BlogListView.as_view(), name="bloglist"),
     
 ]
