from rest_framework import serializers
from apis.accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username", "email", "address", "phone_number", "password"
        extra_kwargs = {
            # "password": {"write_only": True},
            "address": {"required":False},
            "phone_number":{"required":False},
        }

        def create(self, validate_data):
            print('create is called')
            user = User(
                    username = validate_data.get('username'),
                    email = validate_data.get('email', None),
                    address = validate_data.get('address', None),
                    phone_number = validate_data.get('phone_number', None),
                )
            user.set_password(validate_data.get('password'))
            print(validate_data.get('password'))
            print(validate_data)
            user.save()
            return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "email", "address", "phone_number", "password"
        extra_kwargs = {
            "email": {"required":False},
            "address": {"required":False},
            "phone_number": {"required":False},
        }

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.address = validated_data.get('address', instance.address)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.save()
            return instance





