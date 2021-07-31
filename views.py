from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .serializers import AuthorSerializer, BookSerializer, BookSearchSerializer, BookSearchIsbnSerializer
from .models import Book, Author


# Create your views here.

class ListAuthorView(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        return queryset


class ListBookView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CreateAuthor(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookIsbnSearch(generics.CreateAPIView):
    permission_classes = []
    serializer_class = BookSearchIsbnSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(BookIsbn__iexact=self.request.POST.get('BookIsbn'))
        return queryset

    def create(self, request, *args, **kwargs):
        queryset = Book.objects.filter(BookIsbn__iexact=self.request.POST.get('BookIsbn'))
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookSearchAuthor(generics.CreateAPIView):
    permission_classes = []
    serializer_class = BookSearchSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(BookAuthor__FirstName=self.request.POST.get('FirstName'),
                                       BookAuthor__LastName=self.request.POST.get('LastName'))
        return queryset

    def create(self, request, *args, **kwargs):
        queryset = Book.objects.filter(BookAuthor__FirstName=self.request.POST.get('FirstName'),
                                       BookAuthor__LastName=self.request.POST.get('LastName'))

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
