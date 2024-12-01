from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.urls import reverse
from django.views import View, generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from messanger.forms import MessageForm
from messanger.models import Message


def home(request: HttpRequest) -> HttpResponse:
    request.session["test_session_key"] = "our_test_key"
    request.session["new_key"] = "new_key"

    context = {
        "num_messages": Message.objects.count(),
    }

    return render(request, "messanger/home.html", context)


class MessageListView(LoginRequiredMixin, TemplateView):
    template_name = "messanger/message_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MessageForm()

        return context


class MessageDetailView(generic.DetailView):
    model = Message


class MessageCreateView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = MessageForm(request.POST or None)

        if form.is_valid():
            message = form.save()

            return render(
                request, "messanger/message_create_response.html", {"message": message}
            )

        return render(request, "messanger/message_form.html", {"form": form})
