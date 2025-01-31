from rest_framework import serializers 
from .models import Book, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from django.contrib.auth.models import User 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model

# Serializer for Listing Reviews - Display book full details
class ReviewListSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)  # Show full book details
    user = serializers.StringRelatedField()  # Display username instead of ID

    class Meta:
        model = Review
        fields = ['id', 'book', 'rating', 'comment', 'user']  # Include book & user details

# Serializer for Creating Reviews - Accept only Book ID
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'rating', 'comment'] 
        extra_kwargs = {
            'user': {'read_only': True}, 
        }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add `is_staff` to the token response
        data['is_staff'] = self.user.is_staff
        return data