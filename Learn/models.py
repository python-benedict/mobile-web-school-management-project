from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField

# Create your models here.

class User(AbstractUser):
    is_learner = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to= '', default='no-img.jpg', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=6)
    email = models.EmailField(default='none@gmail.com')
    phone_number = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(default='2002-02-22')
    bio = models.TextField()
    city = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5)
    health_issues = models.TextField()
    qualification = models.CharField(max_length=50, default='none')
    Religion = models.CharField(max_length=50, default='Christian')
    Age = models.CharField(max_length=20)
    height = models.CharField(max_length=50)
    level =models.CharField(max_length=50)
    profession = models.CharField(max_length=50, default='Student')
