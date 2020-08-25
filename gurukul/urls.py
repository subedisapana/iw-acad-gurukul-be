from django.urls import path
from gurukul.views import(
    UserView, 
    UserLoginView, PasswordResetRequest,  PasswordTokenCheckAPI, SetNewPasswordAPIView
)
 
app_name = "gurukul"

urlpatterns = [
    path('register/', UserView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('password-reset-request/', PasswordResetRequest.as_view(), name='password-reset-request'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete')
]
