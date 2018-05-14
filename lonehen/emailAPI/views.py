from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions
from django.core.mail import send_mail
from rest_framework import status

# Create your views here.

class Email(APIView):
    def post(self,request, format=None):
        permission_classes = (permissions.AllowAny,)
        data = JSONParser().parse(request)
        send_mail(
            data['from'],
            data['message'],
            "rob@bvzzdesign.com",
            [data['to']],
            fail_silently=False
        )
        return Response(data, status=status.HTTP_201_CREATED)
