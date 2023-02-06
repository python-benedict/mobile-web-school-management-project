from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField


class User(AbstractUser):
    is_learner = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


# Create your models here.
