from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
import uuid

# Create your models here.

class AppUserManager(BaseUserManager):
    def create_user(self, email, display_name, password = None):
        pass
    
    def create_super_user(self, email, display_name, password = None):
        pass
        


class AppUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)
    avatar_url = models.ImageField(upload_to="avatar", blank=True, null=True)
    bio = models.TextField(blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'display_name']
    
    objects = AppUserManager()

