from django.urls import path
from gurukul.views import(
    UserView,
)
 
app_name = "gurukul"

urlpatterns = [
    path('register/', UserView.as_view())
]
