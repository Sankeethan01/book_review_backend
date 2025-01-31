from rest_framework.viewsets import ModelViewSet
from .models import Book, Review
from .serializers import BookSerializer, ReviewListSerializer, ReviewCreateSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import PermissionDenied


# Include is_staff in JWT token for frontend admin check
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["is_staff"] = self.user.is_staff  # Include is_staff for frontend logic
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Book CRUD ViewSet
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow anyone to read, but only authenticated users to add/edit

# Review CRUD ViewSet with proper user assignment
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.select_related("book").all() 
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow reading for all, but only authenticated users can add

    def get_serializer_class(self):
        """Use different serializers for listing and creating"""
        if self.action in ["list", "retrieve"]:  # Use detailed serializer for GET
            return ReviewListSerializer
        return ReviewCreateSerializer  # Use minimal serializer for POST

    def perform_create(self, serializer):
        """Ensure request is authenticated and assign user."""
        if not self.request.user.is_authenticated:
            raise PermissionDenied("User must be authenticated to post a review.")
        serializer.save(user=self.request.user)  # Assign the logged-in user

# User Registration View
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    

# Fetch a single book by ID
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"  # Ensure it matches the URL param


# Fetch all reviews for a specific book
class BookReviewsView(ListAPIView):
    serializer_class = ReviewListSerializer

    def get_queryset(self):
        book_id = self.kwargs.get("id")  # Extract 'id' from the URL
        return Review.objects.filter(book_id=book_id)
