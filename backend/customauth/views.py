from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
from .serializers import UserLoginSerializer, UserProfileSerializer, UserProfileUpdateSerializer, UserRegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
import datetime
from emailer.email_backend import send_email
from rest_framework.exceptions import ValidationError
from customauth.models import CustomUser

class UserRegisterView(GenericViewSet):
    serializer_class = UserRegisterSerializer
    """
    View for user registration.

    Allows users to register by providing email and password.
    """
    @extend_schema(tags=['Authentication'], summary='Register a new user')
    def register(self, request, *args, **kwargs):
        """
        Handle POST requests for user registration.

        Parameters:
        - `request`: The HTTP request object.
        - `args`: Additional arguments passed to the view.
        - `kwargs`: Additional keyword arguments passed to the view.

        Returns:
        - A Response indicating success or failure of the registration.
        """
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()
            return Response({
                'detail': 'User registered successfully',
                'user_data': user_data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(GenericViewSet):
    """
    View for user login.

    Allows users to log in by providing their email and password.
    """
    @extend_schema(tags=['Authentication'], summary='Login a user')
    def login(self, request, *args, **kwargs):
        """
        Handle POST requests for user login.

        Parameters:
        - `request`: The HTTP request object.
        - `args`: Additional arguments passed to the view.
        - `kwargs`: Additional keyword arguments passed to the view.

        Returns:
        - A Response containing the access and refresh tokens upon successful login.
        """
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = authenticate(request, email=email, password=serializer.validated_data['password'])
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)

        # Get the metadata from where the request is coming from
        # including device and IP address
        try:
                user_agent = request.META.get('HTTP_USER_AGENT', None)
                ip_address = request.META.get('REMOTE_ADDR', None)
        except AttributeError:
                print(AttributeError)
                user_agent = None
                ip_address = None

        subscriber_name = email.split('@')[0]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # split date and time
        date, time = current_date.split(' ')
        date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%dth of %B, %Y")
        time = datetime.datetime.strptime(time, "%H:%M:%S").strftime("%I:%M %p")
        formated_time = f"{date} at {time}"
        # Prepare the HTML content from the template
        context = {'subscriber_name': subscriber_name, 'user_agent': user_agent, 'ip_address': ip_address, 'time': formated_time}

        # Send email using the existing backend
        subject = 'HealthSync - Login Alert'
        recipient_list = [email]
        template = 'login_alert.html'

        send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)

class UserLogoutView(GenericViewSet):
    """
    View for user logout.

    Allows users to log out by providing their refresh token.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Authentication'], summary='Logout a user')
    def logout(self, request, *args, **kwargs):
        """
        Handle POST requests for user logout.

        Parameters:
        - `request`: The HTTP request object.
        - `args`: Additional arguments passed to the view.
        - `kwargs`: Additional keyword arguments passed to the view.

        Returns:
        - A Response indicating success or failure of the logout.
        """

        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(request.data.get('refresh'))
                if token:
                    token.blacklist()
                return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'detail': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'detail': 'Both access and refresh tokens are required for logout'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    API view to retrieve details of the user profile.

    Requires authentication for access.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['User Profile'], summary='Access user profile details')
    def get(self, request, *args, **kwargs):
        # Access the UserProfile from the CustomUser instance
        profile = request.user.userprofile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)


class UpdateProfileView(APIView):
    """
    View for updating user profile.

    Allows authenticated users to view and update their profile information.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['User Profile'], summary='Update user profile')
    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests for updating user profile.

        Parameters:
        - `request`: The HTTP request object.
        - `args`: Additional arguments passed to the view.
        - `kwargs`: Additional keyword arguments passed to the view.

        Returns:
        - A Response containing the updated user profile data.
        """
        profile = request.user.userprofile
        if not profile:
            return Response({'detail': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user != profile.user:
            return Response({'detail': 'You are not authorized to update this profile'}, status=status.HTTP_403_FORBIDDEN)
        
        if not request.data:
            return Response({'detail': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        valid_attributes = [
            'first_name', 'last_name', 'about', 'short_description',
            'instagram_link', 'facebook_link', 'twitter_link', 'profile_photo', 'new_password'
        ]
        for key in request.data.keys():
            if key not in valid_attributes:
                raise ValidationError(f"Invalid attribute '{key}'")
        try:
                serializer = UserProfileUpdateSerializer(profile, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response = {
                    'detail': 'Profile updated successfully',
                    'data': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'detail': e.detail}, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['User Profile'], summary='Delete user profile')
    def delete(self, request, *args, **kwargs):
        try:
                user = request.user

                # Retrive the user profile if it exists
                user_profile = getattr(user, 'userprofile', None)
                if user_profile:
                    user_profile.delete()

                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class PasswordResetView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Authentication'], summary='Reset user password')
    def put(self, request, *args, **kwargs):
        profile = request.user.userprofile
        serializer = UserProfileUpdateSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Password reset successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# forget password view
# takes email and send a link to reset password
# link should be valid for 24 hours
# link should be unique for each user
# link should be sent to the user's email
# link should be a one-time use link
# link should be invalidated after use
# link should be invalidated after 24 hours
# link should be invalidated if user changes password
# link should be invalidated if user logs in
class ForgotPasswordView(APIView):
    permission_classes = []

    @extend_schema(tags=['Authentication'], summary='Forgot password')
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            user = CustomUser.objects.get(email=email)
            print("user", user)
            if user:
                users_name = user.first_name 
                # Generate a unique token
                token = RefreshToken.for_user(user)
                # Set the token expiry time
                token.set_exp(lifetime=datetime.timedelta(days=1))
                # Get the metadata from where the request is coming from
                # including device and IP address
                try:
                    user_agent = request.META.get('HTTP_USER_AGENT', None)
                    ip_address = request.META.get('REMOTE_ADDR', None)
                except AttributeError:
                    print(AttributeError)
                    user_agent = None
                    ip_address = None
                # Prepare the HTML content from the template
                context = {'user': user, 'user_agent': user_agent, 'ip_address': ip_address, 'token': token, 'name': users_name}
                # Send email using the existing backend
                subject = 'HealthSync - Reset Password'
                recipient_list = [email]
                template = 'reset_password.html'
                send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)
                return Response({'detail': 'Password reset link sent to your email'}, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)