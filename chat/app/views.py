from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Thread, Message, ThreadUser
from .serializers import (
    ThreadSerializer,
    MessageSerializer,
    MessageUpdateSerializer
)


class ThreadDestroyView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)


class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.method == "POST":
            return Thread.objects.all()
        return [x.thread for x in ThreadUser.objects.filter(user=self.request.user)]


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
