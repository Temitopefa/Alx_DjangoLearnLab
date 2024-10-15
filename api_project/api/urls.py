# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router instance
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the BookViewSet

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for all CRUD operations
    path('', include(router.urls)),
]
