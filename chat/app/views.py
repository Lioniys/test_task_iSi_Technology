from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Thread, Message
from .services import (
    use_limit_participants,
    valid_thread_exists,
    get_relevant_serializer
)
from .serializers import (
    MessageSerializer,
    ThreadSerializer,
    MessageUpdateSerializer,
)


class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """Вариант при котором нужно передавать всех учасников в запросе"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        participants = serializer.validated_data.get("participants")

        use_limit_participants(participants=participants, limit=2)
        obj = valid_thread_exists(participants=participants)
        serializer = get_relevant_serializer(participants=participants, obj=obj)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """Получение списка threads для текущего пользователя"""
        return self.request.user.threads.all()


class ThreadDestroyView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


class MessageUpdateIsReadView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageUpdateSerializer
    permission_classes = (IsOwner,)


class CountMessageNotIsReadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        count = Message.objects.filter(sender=self.request.user, is_read=False).count()
        return Response({"count": count})


class MessagesListInThreadView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        thread = self.kwargs.get("pk")
        user = self.request.user
        return Message.objects.filter(thread=thread, sender=user)
