from django.urls import path, re_path, include
from customauth.views import UserRegisterView,UserLoginView,UpdateProfileView,UserLogoutView,UserProfileView, PasswordResetView, DeleteUserView, ForgotPasswordView

urlpatterns = [
    path('register/', UserRegisterView.as_view({"post": "register"}, name='register')),
    path('login/', UserLoginView.as_view({"post": "login"}), name='login'),
    path('logout/', UserLogoutView.as_view({"post": "logout"}), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),    
    path('profile/get/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/delete/', DeleteUserView.as_view(), name='delete-user'),
    path('forgotpassword/', ForgotPasswordView.as_view(), name='forgot-password'),
]