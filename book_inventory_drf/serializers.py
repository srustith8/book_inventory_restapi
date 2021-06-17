from rest_framework import serializers
from .models import User,Book
from django.contrib.auth import authenticate

from django.contrib.auth.models import update_last_login


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','is_active','is_superuser','is_staff']



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','password']

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id','book_name','author']

class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_name','author']

class BorrowBookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['book_id','date']

