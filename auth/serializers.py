from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'first_name', 'last_name', 'groups', 'projects']
        # Passwords are hashed to no point reading them
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Checking if there are any results of users with the same username
        user_check = User.objects.filter(username=validated_data['username'])
        if user_check.count() > 0:
            raise ValueError("Username in use")

        # Overwriting default create method so we can use the create_user helper function
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
