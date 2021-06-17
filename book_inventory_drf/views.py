from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser
from book_inventory_drf.serializers import RegisterSerializer,UserSerializer,BookListSerializer,BookPostSerializer
from book_inventory_drf.models import User,Book
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
from rest_framework.views import APIView


class ListUsersView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def get(self, request):
        """
        Return a list of all users.
        """
        # usernames = [user.username for user in User.objects.all()]
        data = User.objects.all()
        serializer = UserSerializer(data,many=True).data
        print(serializer)
        return Response(serializer)


class BookListView(APIView):
    serializer_class = BookListSerializer
    permission_classes = (AllowAny,)
    def get(self, request):
        """
        Return a list of all users.
        """
        # usernames = [user.username for user in User.objects.all()]
        data = Book.objects.all()
        serializer = BookListSerializer(data,many=True).data
        print(serializer)
        return Response(serializer)

    def post(self,request):
        data = request.data
        serializer = BookPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'Book added successfully',
            }
        
        return Response(response, status=status_code)


class UserRegistrationView(CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # token = Token.objects.create(user=User.objects.get(name=data['name']))
        # print(token.key)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer_email_data = RegisterSerializer(User.objects.filter(
            email=data['email']),many=True).data
        serializer_pass_data = RegisterSerializer(User.objects.filter(
            password=data['password']), many=True).data
        email = serializer_email_data[0].pop("email")
        token = Token.objects.create(user=User.objects.get(email=data['email']))
        print(token.key)
        try:
            if data['email'] == serializer_email_data[0].pop("email") and data['password'] == serializer_pass_data[0].pop("password"):
                return Response({'message': 'User Login Successfully',"status": status.HTTP_200_OK})
        except:
            return Response({"message": "User authentication failed","status": status.HTTP_401_UNAUTHORIZED})

