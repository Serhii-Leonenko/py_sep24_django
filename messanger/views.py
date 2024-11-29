from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (HttpRequest, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.urls import reverse
from django.views import View, generic
from django.views.decorators.csrf import csrf_exempt

from messanger.forms import MessageForm
from messanger.models import Message


def home(request: HttpRequest) -> HttpResponse:
    request.session["test_session_key"] = "our_test_key"
    request.session["new_key"] = "new_key"

    context = {
        "num_messages": Message.objects.count(),
    }

    return render(request, "messanger/home.html", context)


# def message_list_view(request: HttpRequest) -> HttpResponse:
#     message_list = Message.objects.select_related("user")
#
#     return render(
#         request,
#         "messanger/message_list.html",
#         context={"message_list": message_list}
#     )
class MessageListView(generic.ListView):
    model = Message
    paginate_by = 10

    def get_queryset(self):
        return Message.objects.select_related("user")


# def message_detail_view(request, pk):
#     message = get_object_or_404(Message, pk=pk)
#
#     return render(request, "messanger/message_detail.html", {"message": message})
class MessageDetailView(generic.DetailView):
    model = Message


def json_message_list(request):
    messages = list(Message.objects.values("id", "message"))

    return JsonResponse(messages, safe=False)


def message_create_view(request: HttpRequest) -> HttpResponse:
    context = {}
    form = MessageForm(request.POST or None)

    if form.is_valid():
        user_id = form.cleaned_data.pop("user_id") or request.user.pk
        message = Message(**form.cleaned_data)
        message.user_id = user_id
        message.save()

        return HttpResponseRedirect(reverse("user-messages", args=(user_id, )))

    context["form"] = form

    return render(request, "messanger/message_form.html", context=context)

class UserMessagesView(View):
    def get(self, request, pk):
        messages = Message.objects.filter(user_id=pk)

        return render(
            request,
            "messanger/partials/user_messages.html",
            {
                "messages": messages,
            }
        )
