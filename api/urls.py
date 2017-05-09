from django.conf.urls import url
from .views import StudentList, StudentDetail

urlpatterns = [
    url(r'students/$', StudentList.as_view()),
    url(r'students/(?P<name>[a-zA-Z]+)/$', StudentDetail.as_view()),
]
