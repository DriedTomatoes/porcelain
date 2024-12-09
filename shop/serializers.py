from rest_framework.serializers import ModelSerializer
from .models import Client

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['email','password', 'username', 'first_name', 'last_name', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


