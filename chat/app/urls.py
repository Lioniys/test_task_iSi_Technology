from django.urls import path
from .views import (
    ThreadListCreateView,
    ThreadDestroyView,
    MessageListCreateView,
    MessageIsReadView,
    MessageNotIsReadView
)


urlpatterns = [
    path("threads/", ThreadListCreateView.as_view()),
    path("threads/<int:pk>/", ThreadDestroyView.as_view()),
    path("messages/", MessageListCreateView.as_view()),
    path("messages/<int:pk>/", MessageIsReadView.as_view()),
    path("messagesnotisread", MessageNotIsReadView.as_view()),
]
