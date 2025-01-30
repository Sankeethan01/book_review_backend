from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    BookViewSet,
    ReviewViewSet,
    RegisterView,
    CustomTokenObtainPairView,
    BookDetailView,
    BookReviewsView,
)

# Create a router and register API routes
router = DefaultRouter()
router.register('books', BookViewSet)  # URL: /api/books/
router.register('reviews', ReviewViewSet)  # URL: /api/reviews/

urlpatterns = [
    # Include router URLs
    path('', include(router.urls)),

    # Authentication endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Book Detail & Reviews (Ensure lookup_field="id" in views.py)
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:id>/reviews/', BookReviewsView.as_view(), name='book-reviews'),
]
