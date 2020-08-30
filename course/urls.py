from django.urls import path
from .views import CourseView, UserCourseView

urlpatterns = [
    path('', CourseView.as_view()),
    path('user/<int:user_id>/', UserCourseView.as_view())
]
