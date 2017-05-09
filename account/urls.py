from django.conf.urls import url
from .views import AccountDetail

urlpatterns = [
    url(r'register/$', AccountDetail.as_view()),
]
