from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notice.views import NoticeView, NoticeObjectView 

urlpatterns = [
    path('', NoticeView.as_view()),
    path('<int:pk>/', NoticeView.as_view()),
    path('notice/<int:pk>/', NoticeObjectView.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
