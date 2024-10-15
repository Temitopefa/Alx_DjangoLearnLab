# api/views.py

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer to convert model data to JSON


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer