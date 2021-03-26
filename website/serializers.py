from tokenize import TokenError

from django.contrib.auth.password_validation import validate_password
from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from website.models import User


class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, validators=[validate_password], required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [

            'full_name',
            'email',
            'password',
            'confirm_password',
            'individual',

        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')