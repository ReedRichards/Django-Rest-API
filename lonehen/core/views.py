from core.models import (AboutPage,
                         Carousel,
                         Press,
                         Event,
                         BlogPost,
                         MakersNotes,
                         ShopItem)
from core.serializers import (AboutSerializer,
                              UserSerializer,
                              CreateUser,
                              CarouselSerializer,
                              PressSerializers,
                              EventSerializer,
                              BlogPostSerializer,
                              MakersNotesSerializer,
                              ShopItemSerializer)
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from core.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from django.core.mail import send_mail
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class Checkout(APIView):
    def post(self, request,format=None):
        permission_classes = (permissions.AllowAny,)
        data = JSONParser().parse(request)
        try:
            charge = stripe.Charge.create(
                amount = data["total"],
                currency = "usd",
                source = data["token"],
                description = "new charge"
            )
            
            return Response(data, status=status.HTTP_201_CREATED)
        except stripe.error.CardError as ce:
            return Response(ce,status=status.HTTP_500_INTERNAL_SERVER_ERROR )

## this is going to be left here for compatibility reasons
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

class LoginToLonehen(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request, format=None):
        return Response({"details":"Valid"})


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = CreateUser

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AboutPageView(generics.ListCreateAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AboutPageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class CarouselList(generics.ListCreateAPIView):
    queryset = Carousel.objects.all()
    serializer_class=CarouselSerializer
    authentication_classes = (TokenAuthentication,)
    permissions_classes =(permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CarouselDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class PressList(generics.ListCreateAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class=EventSerializer
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly) 

class BlogList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class MakersNotesList(generics.ListCreateAPIView):
    queryset = MakersNotes.objects.all()
    serializer_class = MakersNotesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MakersNotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MakersNotes.objects.all()
    serializer_class = MakersNotesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class ShopItemList(generics.ListCreateAPIView):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ShopItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
