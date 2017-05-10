# coding=utf-8
import re

from rest_framework import serializers

from django.contrib.auth.models import User


class AccountFrom(object):
    def __init__(self, email, username, password, repeat_password):
        self.email = email
        self.username = username
        self.password = password
        self.repeat_password = repeat_password


class AccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def create(self, validated_data):
        User.objects.create_user(username=validated_data.get('username'),
                                 email=validated_data.get('email'),
                                 password=validated_data.get('password'))
        return AccountFrom(username=validated_data.get('username'),
                           email=validated_data.get('email'),
                           password=validated_data.get('password'),
                           repeat_password=validated_data.get('repeat_password'))

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        # User.objects.update()
        instance.save()
        return instance

    
    def validate_email(self, value):
        try:
            result_email = User.objects.get(email=value)
        except User.DoesNotExist:
            return value
        raise serializers.ValidationError('该邮箱已注册')

    def validate_password(self, value):
        self.password = value
        if re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$', value):
            return value
        else:
            raise serializers.ValidationError('密码必须由6-20个字母和数字组成')

    def validate_repeat_password(self, value):
        self.repeat_password = value
        if self.password and value and self.password != value:
            raise serializers.ValidationError("两次输入的值不相同")
        return value

    def validate_username(self, value):
        if re.match("^[A-Za-z][A-Za-z0-9_.]*$", value):
            return value
        else:
            raise serializers.ValidationError("用户名只能有数字字母下划线组成")
