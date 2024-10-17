# api/models.py

from django.db import models

class Author(models.Model):
    """
    The Author model represents a book author.
    It contains a 'name' field to store the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    The Book model represents a book.
    It includes a title, publication year, and a foreign key linking to an author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
