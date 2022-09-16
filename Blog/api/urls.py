from django.urls import path
from Blog.api.views import CategoryAPI,BlogAPI,CategoryUpdateDeleteAPI


urlpatterns = [
    path('categories/', CategoryAPI.as_view(), name='api_categories'),
    path('blogs/', BlogAPI.as_view(), name='api_blogs'),
    # path('categories/destroy/<int:pk>/', CategoryDestroyView.as_view(), name='api_categories_delete'),
    path('categories/<int:pk>/', CategoryUpdateDeleteAPI.as_view(), name='api_categories'),
]