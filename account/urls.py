from django.urls import path, include
from .views import (
    MyTokenObtainPairView, 
    UserRegister,
    EditProfile,
    VertifyEmail, 
    ActiveUserWithEmail,
    PasswordResteRequest,
    UserLogout,
)

app_name = 'account'

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegister.as_view(), name='register'),
    path('update_profile/', EditProfile.as_view(), name='update_profile'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('vertify_email/', VertifyEmail.as_view(), name='vertify_email'),
    path('active_user/', ActiveUserWithEmail.as_view(), name='active_user'),
    path('password_reset_request', PasswordResteRequest.as_view(), name='password_reset_request'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
