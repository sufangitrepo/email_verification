from rest_framework.serializers import ModelSerializer
from .models import MyUser


class MyUserRegisterSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['email','password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        my_user:MyUser = MyUser(**validated_data)
        my_user.set_password(raw_password=password)
        my_user.save()
        return my_user
    


class UserLoginSerializer(ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ['email', 'id']

