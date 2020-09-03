from django.urls import path
from assignment.views import AssignmentView, AssignmentAnswerView

 
app_name = "assignment"

urlpatterns = [
     path('', AssignmentView.as_view()),
     path('<int:pk>/', AssignmentView.as_view()),
     path('answers/', AssignmentAnswerView.as_view()),
     path('answers/<int:pk>/', AssignmentAnswerView.as_view())
]
