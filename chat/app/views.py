from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . import permissions, models, serializers, services


class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = models.Thread.objects.all()
    serializer_class = serializers.ThreadSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """A variant in which it is necessary to pass all participants in the query"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        participants = serializer.validated_data.get("participants")

        services.use_limit_participants(participants=participants, limit=2)
        obj = services.valid_thread_exists(participants=participants)
        serializer = services.get_relevant_serializer(participants=participants, obj=obj)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """Getting the list of threads for the current user"""
        return self.request.user.threads.all()


class ThreadDestroyView(generics.DestroyAPIView):
    queryset = models.Thread.objects.all()
    serializer_class = serializers.ThreadSerializer
    permission_classes = (IsAuthenticated,)


class MessageCreateView(generics.CreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = (IsAuthenticated,)


class MessageUpdateIsReadView(generics.UpdateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageUpdateSerializer
    permission_classes = (permissions.IsOwner,)


class CountMessageNotIsReadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        count = models.Message.objects.filter(sender=self.request.user, is_read=False).count()
        return Response({"count": count})


class MessagesListInThreadView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        thread = self.kwargs.get("pk")
        user = self.request.user
        return models.Message.objects.filter(thread=thread, sender=user)
