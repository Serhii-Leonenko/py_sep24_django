from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView

from messanger.models import Message


class PartialMessagesView(LoginRequiredMixin, FilterView):
    template_name = "messanger/partials/partial_message_list.html"
    paginate_by = 10
    model = Message
    filterset_fields = ["user"]

    def get_queryset(self):
        return Message.objects.select_related("user").order_by("id")
