from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from .serializers import ClientSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        r_data = request.data

        if r_data['password'] != r_data['password_confirm']:
            raise exceptions.APIException('Passwords do not match')

        serializer = ClientSerializer(data=r_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)



# Create your views here.
