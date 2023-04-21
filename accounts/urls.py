from django.urls import path

from .views import UserRegisterView, UserLoginView, VerifyEmailView


urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('verify/<str:uid>', VerifyEmailView.as_view()),
]