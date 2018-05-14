from django.db import models
import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import JSONField
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.

class AboutPage(models.Model):
    about_title = models.TextField(blank=True)
    about_description = models.TextField(blank=True)
    about_raw = JSONField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='aboutpage', on_delete=models.CASCADE)

class Carousel(models.Model):
    carousel_images = models.ImageField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='carousel', on_delete=models.CASCADE)


class Press(models.Model):
    press_image=models.ImageField(blank=True)
    press_descritption=models.TextField(blank=True)
    press_raw = JSONField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='press', on_delete=models.CASCADE)


class Event(models.Model):
    event_title = models.CharField(blank=True,max_length=255)
    event_start_time = models.CharField(blank=True,max_length=255)
    event_end_time = models.CharField(blank=True,max_length=255)
    event_start_date = models.DateTimeField( default=datetime.date.today)
    event_end_date = models.DateTimeField( default=datetime.date.today)
    event_details = models.TextField(blank=True)
    event_raw = JSONField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='aboutpage', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='event', on_delete=models.CASCADE)

    @property
    def is_past_due(self):
        return datetime.date.today() > self.event_end_date.date()

    @property
    def is_multi_day(self):
        return self.eventStartDate.day < self.event_end_date.day

class BlogPost(models.Model):
    post_title = models.CharField(blank=True,max_length=255)
    post_date = models.DateTimeField(("Date Published"), default=datetime.date.today)
    post_body = models.TextField(blank=True)

    owner = models.ForeignKey('auth.User', related_name='blogpost', on_delete=models.CASCADE)

class MakersNotes(models.Model):
    wine_image = models.ImageField(blank=True)
    item_title = models.CharField(blank=True,max_length=255)
    item_description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='makersnotes', on_delete=models.CASCADE)

class ShopItem(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    raw_description = JSONField()
    image = models.ImageField(blank=True)
    quantity = models.IntegerField(default=0)
    category = models.CharField(blank=True, max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey('auth.User', related_name='shopitem', on_delete=models.CASCADE)


