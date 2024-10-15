# api/views.py

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer to convert model data to JSON


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Authentication is enforced via TokenAuthentication.
    Only authenticated users are allowed to access this viewset.
    """
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 