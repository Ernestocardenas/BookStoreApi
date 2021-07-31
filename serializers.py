from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('FirstName', 'LastName', 'Biography', 'Publisher', )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('BookIsbn','BookName','BookPrice','BookAuthor','BookGenre','Publisher','PublishedYear','CopiesSold',)

class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('FirstName', 'LastName',)

class BookSearchIsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('BookIsbn', )