from django.contrib.auth.models import User
from rest_framework import serializers

from task_1.models import Transaction


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        """Serializing User model by defined fields"""
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="first_name", read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'amount', 'date')


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionByDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'date', )
