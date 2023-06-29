from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "username"


class YourStory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, blank=True)
    caption = models.TextField(max_length=255, blank=True)
    story = models.TextField(blank=True, null=True)
    author = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='picture')
    date = models.DateTimeField(null=True, blank=True)

class ContactUs(models.Model):  ####################contact
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    msg = models.CharField(max_length=255, blank=True)


class YourTrip(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, blank=True)
    tagline = models.TextField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='picture')