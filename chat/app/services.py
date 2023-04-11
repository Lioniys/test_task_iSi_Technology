from rest_framework import serializers
from .models import ThreadUser


def use_limit_participants(participants: list, limit: int):
    if len(participants) > limit:
        raise serializers.ValidationError("There can only be two participants in the thread")


def valid_thread_exists(participant, user):
    queryset1 = ThreadUser.objects.filter(user=user)
    queryset2 = ThreadUser.objects.filter(user=participant.get("user"))
    list_obj_thread = [obj.thread for obj in queryset2]
    for obj in queryset1:
        if obj.thread in list_obj_thread:
            return obj.thread
