from .models import *
from rest_framework import serializers


class Chatroom_serializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"


class message_serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Message
        fields = "__all__"
