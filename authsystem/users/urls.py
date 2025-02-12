from django.urls import path
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView,)
from .views import RegisterView,UserDetailView,LogoutView

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('/login',TokenObtainPairView.as_view(),name='token_obtain'),
    path('login/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('user_detail/',UserDetailView.as_view(),name='user_detail'),
]