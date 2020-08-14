from django.urls import path
from gurukul.views import(
    UserView, 
    UserLoginView
)
 
app_name = "gurukul"

urlpatterns = [
    path('register/', UserView.as_view()),
     path('login/', UserLoginView.as_view())
]
