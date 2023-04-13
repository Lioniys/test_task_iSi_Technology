from django.urls import path
from .views import (
    ThreadListCreateView,
    ThreadDestroyView,
    MessageCreateView,
    MessageUpdateIsReadView,
    CountMessageNotIsReadView,
    MessagesListInThreadView,
)


urlpatterns = [
    path("threads/", ThreadListCreateView.as_view()),
    path("threads/<int:pk>/", ThreadDestroyView.as_view()),
    path("messages/", MessageCreateView.as_view()),
    path("messages/<int:pk>/", MessageUpdateIsReadView.as_view()),
    path("messagesinthread/<int:pk>/", MessagesListInThreadView.as_view()),
    path("count/", CountMessageNotIsReadView.as_view()),
]
