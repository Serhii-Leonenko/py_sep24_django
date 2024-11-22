from django.urls import path

from messanger.views import home, MessageListView, MessageDetailView, json_message_list, message_create_view, \
    UserDetailView, UserMessagesView

urlpatterns = [
    path("home/", home, name="home"),
    path("messages/", MessageListView.as_view(), name="message-list"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
    path("json-messages/", json_message_list, name="json-message-list"),
    path(
        "messages/create/",
        message_create_view,
        name="message-create"
    ),
    path("users/<int:pk>/",  UserDetailView.as_view(), name="user-detail"),
    path("users/<int:pk>/messages/", UserMessagesView.as_view(), name="user-messages")
]
