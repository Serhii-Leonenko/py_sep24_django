from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from messanger.models import Message


class PartialMessagesView(LoginRequiredMixin, generic.ListView):
    template_name = "messanger/partials/partial_message_list.html"
    paginate_by = 10
    model = Message

    def get_queryset(self):
        user = self.request.GET.get("user")
        queryset = Message.objects.select_related("user").order_by("id")

        if user:
            queryset = queryset.filter(user_id=user)

        return queryset
