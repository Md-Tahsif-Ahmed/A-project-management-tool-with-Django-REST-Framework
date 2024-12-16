from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserDetailView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # Update User Details
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    # Delete User Account
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
