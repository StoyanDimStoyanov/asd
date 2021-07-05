from django.urls import path
from demo.views import UserDetailsApiView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('create/', UserDetailsApiView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
