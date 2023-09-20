from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        Model = CustomUser
        fields = ['firstname', 'lastname', 'email', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = CustomUser(
            firstname = validated_data['firstname'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user