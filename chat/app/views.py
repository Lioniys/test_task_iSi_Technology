from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Thread, Message, ThreadUser
from .serializers import (
    ThreadSerializer,
    MessageSerializer,
    MessageUpdateSerializer
)


class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        if self.request.method == "POST":
            return Thread.objects.all()
        return [x.thread for x in ThreadUser.objects.filter(user=self.request.user)]


class ThreadDestroyView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params is not None:
            thread = self.request.query_params.get("thread")
            return Message.objects.filter(thread=thread)
        return Message.objects.all()


class MessageIsReadView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageUpdateSerializer
    permission_classes = (IsAuthenticated,)


class MessageNotIsReadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        count = len(Message.objects.filter(sender=user, is_read=False))
        return Response({"count": count})
