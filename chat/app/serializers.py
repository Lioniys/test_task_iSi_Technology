from rest_framework import serializers
from .models import Thread, Message
# from django.contrib.auth import get_user_model


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ['text', 'thread', 'sender', 'time_created']


class MessageUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.is_read = validated_data.get("is_read", instance.is_read)
        instance.save()
        return instance

    class Meta:
        model = Message
        fields = ['is_read']

# class ThreadCreateSerializer(serializers.Serializer):
#     participants = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')
