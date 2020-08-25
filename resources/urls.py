from django.urls import path
from resources.views import ResourcesView
urlpatterns=[
     path('', ResourcesView.as_view()),
]