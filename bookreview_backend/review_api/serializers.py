from rest_framework import serializers
from .models import Book, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model

class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()  # Add a method field for book details

    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'rating', 'comment', 'created_at']

    def get_book(self, obj):
        # Return book details including the title
        return {
            "id": obj.book.id,
            "title": obj.book.title
        }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add `is_staff` to the token response
        data['is_staff'] = self.user.is_staff
        return data