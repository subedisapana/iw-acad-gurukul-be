from django.urls import path
from gurukul.views import(
    api_user_view,
)
 
app_name = "gurukul"

urlpatterns = [
    path('register/', api_user_view)
]
