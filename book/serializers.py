from rest_framework import serializers
from book.models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description')
