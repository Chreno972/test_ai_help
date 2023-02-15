from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    topics = models.TextField(null=True)
    hours_worked = models.PositiveIntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    age = models.PositiveIntegerField(null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    users = models.ManyToManyField(User, related_name='topics_followed')

    def __str__(self):
        return self.name


class Hours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.topic.name} - {self.hours} hours"


# Path: authentication\serializers.py
# from rest_framework import serializers
# from .models import User, Topic

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'age', 'country', 'city', 'topics', 'is_student', 'is_dev')

# class TopicSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Topic
#         fields = ('id', 'name')

# # Path: authentication\views.py
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .serializers import UserSerializer, TopicSerializer
# from .models import User, Topic

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save()

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save()

# class TopicList(generics.ListCreateAPIView):
#     queryset = Topic.objects.all()
#     serializer_class = TopicSerializer
#     permission_classes = (IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save()

# class TopicDetail(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Topic.objects.all()
#     serializer_class = TopicSerializer
#     permission_classes = (IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save()

# # Path: authentication\urls.py
# from django.urls import path
# from .views import UserList, UserDetail, TopicList, TopicDetail

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('topics/', TopicList.as_view()),
#     path('topics/<int:pk>/', TopicDetail.as_view()),
# ]

# # Path: authentication\urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [

#     path('admin/', admin.site.urls),
#     path('api/', include('authentication.urls')),
# ]

# # Path: authentication\settings.py
# from pathlib import Path
# import os


# BASE_DIR = Path(__file__).resolve().parent.parent





