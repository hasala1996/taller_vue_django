from .models import Book, Author
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


class AuthorSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Book
        fields = ('title','description','id_author')
        expandable_fields = {
            'id_author':AuthorSerializer
            }

        