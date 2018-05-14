from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('about-page/', views.AboutPageView.as_view()),
    path('email/', views.Email.as_view()),
    path('checkout/', views.Checkout.as_view()),
    path('about-page/<int:pk>/', views.AboutPageDetail.as_view()),
    path('carousel/',views.CarouselList.as_view()),
    path('carousel/<int:pk>/',views.CarouselDetail.as_view()),
    path('press/',views.PressList.as_view()),
    path('press/<int:pk>/',views.PressDetail.as_view()),
    path('event/',views.EventList.as_view()),
    path('event/<int:pk>/',views.EventDetail.as_view()),
    path('blog/',views.BlogList.as_view()),
    path('blog/<int:pk>/',views.BlogDetail.as_view()),
    path('makersnotes/',views.MakersNotesList.as_view()),
    path('makersnotes/<int:pk>/',views.MakersNotesDetail.as_view()),
    path('shop/',views.ShopItemList.as_view()),
    path('shop/<int:pk>/',views.ShopItemDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/login/', views.LoginToLonehen.as_view()),
    path('users/register/', views.CreateUserView.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]
