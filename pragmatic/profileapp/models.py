from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
# Profile객체와 user객체를 1:1로 커넥팅, CASCADE: user 객체 사라질 때 Profile삭제
    image = models.ImageField(upload_to="profile/", null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)