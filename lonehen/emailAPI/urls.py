from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from emailAPI import views


urlpatterns=[
    path('', views.Email.as_view()),
]
