from django.urls import path
from .views import (
    ThreadListCreateView,
    ThreadDestroyView,
    MessageCreateView,
    MessageIsReadView,
    MessageNotIsReadView
)


urlpatterns = [
    path("threads/", ThreadListCreateView.as_view()),
    path("threads/<int:pk>/", ThreadDestroyView.as_view()),
    path("messages/", MessageCreateView.as_view()),
    path("messages/<int:pk>/", MessageIsReadView.as_view()),
    path("messagesnotisread", MessageNotIsReadView.as_view()),
]
