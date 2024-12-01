from django.urls import path

from messanger.views.json_views import json_message_list
from messanger.views.partial_views import PartialMessagesView
from messanger.views.template_views import (
    MessageCreateView,
    MessageDetailView,
    MessageListView,
    home,
)

template_urlpatterns = [
    path("", home, name="home"),
    path("messages/", MessageListView.as_view(), name="message-list"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
    path("messages/create/", MessageCreateView.as_view(), name="message-create"),
]

partial_urlpatterns = [
    path(
        "messages/partial/", PartialMessagesView.as_view(), name="partial-message-list"
    ),
]

json_urlpatterns = [
    path("json-messages/", json_message_list, name="json-message-list"),
]

urlpatterns = template_urlpatterns + partial_urlpatterns + json_urlpatterns
