from django.urls import path
from gurukul.views import(
    UserView, 
    UserLoginView,
    UserRegisterView
)
 
app_name = "gurukul"

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
     path('login/', UserLoginView.as_view()),
     path('<int:pk>/', UserView.as_view()),
]
