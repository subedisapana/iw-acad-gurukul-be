from django.urls import path, include
from gurukul.views import(
    UserView,
    UserLoginView,
    UserRegisterView,
    ChangePasswordView
)
 
app_name = "gurukul"

urlpatterns = [

     path('register/', UserRegisterView.as_view()),
     path('login/', UserLoginView.as_view()),
     path('<int:pk>/', UserView.as_view()),
     path('change-password/', ChangePasswordView.as_view(), name='change-password'),
     path('password_reset/', include('django_rest_passwordreset.urls',namespace='password_reset')),
]
