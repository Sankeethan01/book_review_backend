from rest_framework import serializers
from .models import Book, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'rating', 'comment', 'user']  # ✅ Include 'user'
        extra_kwargs = {'user': {'read_only': True}}  # ✅ Ensure 'user' is read-only

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add `is_staff` to the token response
        data['is_staff'] = self.user.is_staff
        return data