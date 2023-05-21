from rest_framework import serializers


class SendForgotPasswordCodeSerializer(serializers.Serializer):
    email = serializers.CharField()


class CheckForgotPasswordCodeSerializer(serializers.Serializer):
    email = serializers.CharField()
    code = serializers.CharField()


class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    code = serializers.CharField()
    new_password = serializers.CharField()
