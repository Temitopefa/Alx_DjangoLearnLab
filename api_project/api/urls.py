# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token

# Create a router instance
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the BookViewSet

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # Include the router URLs for all CRUD operations
    path('', include(router.urls)),
]
