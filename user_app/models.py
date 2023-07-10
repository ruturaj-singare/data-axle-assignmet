from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from utils.constants import *


class User(AbstractUser):
    """
        Class for store abstract user. 
    """
    user_id = models.BigAutoField(
        primary_key=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)

    objects = UserManager()

    username = None
    USERNAME_FIELD = USERNAME_FIELD_PHONE_USER_MODEL
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone} -> {self.first_name + self.last_name} -> {self.user_id}"

