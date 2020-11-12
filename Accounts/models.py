import datetime
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, active=True):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not first_name:
            raise ValueError("Users must have a First name")
        if not last_name:
            raise ValueError("Users must have a Last name")
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user_obj.set_password(password)
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email,  first_name, last_name,password=None, active=True):
        user_obj = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user_obj.admin = True
        user_obj.staff = True
        return user_obj 

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name}  {self.last_name}'
    
    def __str__(self):
        return self.email

    @property
    def is_active(self):
        return self.active
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_staff(self):
        return self.staff