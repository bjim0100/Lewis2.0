from django.urls import path

from website.views import SignUpView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/signup/', SignUpView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='refreshtoken'),
]
