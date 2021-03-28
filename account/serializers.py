from django.contrib.auth.models import User
from rest_framework import serializers

from account import models as auth


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth.UserDetail
        fields = (
            'role',
            'user',
            'name',
            "email",
            'phone_no',
        )