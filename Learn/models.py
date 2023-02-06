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


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.content
    

class Course(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default='#007bff')
    
    def __str__(self):
        return self.name
    
    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class ="badge badge-primary" style="background-color:'
        return mark_safe(html)
        

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumb = models.ImageField(upload_to='',null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='No Title')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.EmbedVideoField(blank=True, Null=True)
    

class Notes(models.Model):
    title = models.CharField(max_length=255, default='No Title')
    file = models.FieldFile(upload_to='', null=True, blank=True)
    cover = models.ImageField(upload_to='', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
        

class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners')
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    
    def __str__(self):
        return self.name
    
    

