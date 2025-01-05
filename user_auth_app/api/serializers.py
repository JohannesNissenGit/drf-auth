from django.contrib.auth.models import User
from rest_framework import serializers

from user_auth_app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']


class RegistrationSerializer(serializers.ModelSerializer):
    requested_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'requested_password']
        extra_kwargs = {
            'password': {'write_only': True}  # make password write only
        }

    def save(self):
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        pw = self.validated_data['password']
        requested_pw = self.validated_data['requested_password']

        if pw != requested_pw:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        if User.objects.filter(username=account.username).exists():
            raise serializers.ValidationError({'username': 'Username exists already.'})

        if User.objects.filter(email=account.email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use.'})

        account.set_password(pw)
        account.save()
        return account
