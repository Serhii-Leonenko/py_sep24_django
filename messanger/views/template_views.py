from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View, generic
from django.views.generic import TemplateView

from messanger.forms import MessageForm
from messanger.models import Message


@login_required()
def home(request: HttpRequest) -> HttpResponse:
    num_messages = Message.objects.count()
    num_visits = request.session.get("num_visits", 1)
    last_visit = request.session.get("last_visit", timezone.now().isoformat())

    context = {
        "num_messages": num_messages,
        "num_visits": num_visits,
        "last_visit": last_visit,
    }

    request.session["num_visits"] = num_visits + 1
    request.session["last_visit"] = timezone.now().strftime("%Y-%m-%d %H:%M")

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
