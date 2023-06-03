from rest_framework import serializers
from .serializers import ThreadSerializer
from .models import Thread


def use_limit_participants(participants: list, limit: int):
    """Limiting transferred users"""
    if len(participants) > limit:
        raise serializers.ValidationError(f"There can only be {limit} participants in the thread")


def valid_thread_exists(participants):
    """Checking if there is a thread, works only if there are two participants"""
    if len(participants) == 2:
        user1, user2 = participants
        queryset1 = user1.threads.all()
        queryset2 = user2.threads.all()
        for obj in queryset1:
            if obj in queryset2:
                return obj


def get_relevant_serializer(participants, obj):
    """Returns the serializer of either a created object or an existing one"""
    if obj is not None:
        return ThreadSerializer(obj)
    obj = Thread.objects.create()
    obj.participants.add(*participants)
    return ThreadSerializer(obj)
