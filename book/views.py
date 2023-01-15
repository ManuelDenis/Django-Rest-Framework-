from django.shortcuts import render
from rest_framework import viewsets, generics
from book.models import Book
from book.serializers import BookSerializers


class BookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
