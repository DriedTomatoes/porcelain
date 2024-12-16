from django.db.migrations import serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from .serializers import ClientSerializer
from .serializers import ProductSerializer
from .models import User,Product
from django.http import HttpResponse
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self, request):
        r_data = request.data

        if r_data['password'] != r_data['password_confirm']:
            raise exceptions.APIException('Passwords do not match')

        serializer = ClientSerializer(data=r_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
            username = request.data['username']
            password = request.data['password']

            client = Client.objects.filter(username=username).first()
            if client is None:
                raise exceptions.AuthenticationFailed('Client does not exist')

            if not client.check_password(password):
                raise exceptions.AuthenticationFailed('Invalid password')

            serializer = ClientSerializer(client)

            return Response(serializer.data)
# Create your views here.

def create_product(request):
     serializer = ProductSerializer(request.data)
     if serializer.is_valid():
          serializer.save()
          return Response({
               "status": "success",
               "message" : "Produkt zostal utworzony pomyslnie",
               "data" : serializer.data
          }, status=status.HTTP_201_CREATED)
     else:
          return Response({
               "status" : "error",
               "message" : "Blad walidacji",
               "errors" : serializer.errors
          }, status= status.HTTP_400_BAD_REQUEST)