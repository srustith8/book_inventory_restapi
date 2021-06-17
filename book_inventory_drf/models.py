from django.db import models
import uuid
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import AbstractUser

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserManager(BaseUserManager):
    '''
    creating a manager for a custom user model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
    '''
    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# class User(AbstractBaseUser,PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255,null=True)  
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True
#         )
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

#     def __str__(self):
#         return self.email

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True,unique=True)  
    password= models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True,)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    
    def __str__(self):
        return self.book_name

class CustomerOrder(models.Model):
    login_name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    booksborrowed = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    book_count = models.IntegerField(default=0,)
    date = models.DateField()