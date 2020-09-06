from django.urls import path, include
from gurukul.views import(
    UserView,
    UserLoginView,
    UserRegisterView,
    ChangePasswordView,
    InstructorRequestView,
)
 
app_name = "gurukul"

urlpatterns = [

     path('register/', UserRegisterView.as_view()),
     path('login/', UserLoginView.as_view()),
     path('<int:pk>/', UserView.as_view()),
     path('change-password/', ChangePasswordView.as_view(), name='change-password'),
     path('instructor-request/', InstructorRequestView.as_view())
     ]
