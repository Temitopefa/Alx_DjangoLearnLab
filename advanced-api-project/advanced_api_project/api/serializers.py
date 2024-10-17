# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    The BookSerializer serializes all fields of the Book model and includes
    validation to ensure that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    The AuthorSerializer serializes the 'name' field of the Author model and
    includes a nested BookSerializer to serialize the related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
