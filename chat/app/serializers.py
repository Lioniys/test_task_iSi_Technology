from rest_framework import serializers
from .services import use_limit_participants, valid_thread_exists
from .models import Thread, Message, ThreadUser


class ThreadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadUser
        fields = ['user']


class ThreadSerializer(serializers.ModelSerializer):
    participants = ThreadUserSerializer(many=True)

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        user = validated_data.get("user")
        use_limit_participants(participants=participants, limit=1)
        obj = valid_thread_exists(participant=participants[0], user=user)
        if obj is not None:
            return obj
        obj = Thread.objects.create()
        ThreadUser.objects.create(user=user, thread=obj)
        for participant in participants:
            ThreadUser.objects.create(user=participant.get("user"), thread=obj)
        return obj

    class Meta:
        model = Thread
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ['text', 'thread', 'sender']


class MessageUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.is_read = validated_data.get("is_read", instance.is_read)
        instance.save()
        return instance

    class Meta:
        model = Message
        fields = ['is_read']
