from django.urls import path
from assignment.views import AssignmentView

 
app_name = "assignment"

urlpatterns = [
     path('', AssignmentView.as_view()),
]