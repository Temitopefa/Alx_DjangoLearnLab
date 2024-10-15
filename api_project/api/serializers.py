# api/serializers.py

from rest_framework import serializers
from .models import Book  # Assuming Book model is already defined

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # This includes all fields of the Book model
