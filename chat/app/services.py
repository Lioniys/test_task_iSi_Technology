from rest_framework import serializers
from .models import ThreadUser, Thread


def use_limit_participants(participants: list, limit: int):
    """Ограничение передаваемых пользователей"""
    if len(participants) > limit:
        raise serializers.ValidationError(f"There can only be {limit + 1} participants in the thread")


def create_thread(participants, user):
    """Создает поток и связывает его с моделью User"""
    obj = Thread.objects.create()
    ThreadUser.objects.create(user=user, thread=obj)
    for participant in participants:
        ThreadUser.objects.create(user=participant.get("user"), thread=obj)
    return obj

def valid_thread_exists(participants, user):
    """Проверка существует ли поток, работает только если учасников двое"""
    if len(participants) == 1:
        queryset1 = ThreadUser.objects.filter(user=user)
        queryset2 = ThreadUser.objects.filter(user=participants[0].get("user"))
        list_obj_thread = [obj.thread for obj in queryset2]
        for obj in queryset1:
            if obj.thread in list_obj_thread:
                return obj.thread
