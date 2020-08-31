from django.urls import path
from resources.views import ResourceView

urlpatterns=[
     path('', ResourceView.as_view()),
     path('<int:pk>/', ResourceView.as_view()),
]
