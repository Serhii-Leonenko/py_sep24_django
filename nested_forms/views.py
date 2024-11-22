from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.list import ListView

from nested_forms.forms import ChildFormset
from nested_forms.models import Parent


class ParentListView(ListView):
    model = Parent

    def get_queryset(self):
        return Parent.objects.prefetch_related("children")


class ParentCreateView(generic.CreateView):
    model = Parent
    fields = ["name"]
    success_url = reverse_lazy("nested_forms:parent-list")
    template_name = "nested_forms/parent_form_js.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["children_form"] = ChildFormset(self.request.POST or None)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        children_form = context["children_form"]

        with transaction.atomic():
            self.object = form.save() # create parent

            if children_form.is_valid():
                children_form.instance = self.object
                children_form.save()

        return HttpResponseRedirect(self.get_success_url())


class ParentUpdateView(generic.UpdateView):
    model = Parent
    fields = ["name"]
    success_url = reverse_lazy("nested_forms:parent-list")
    template_name = "nested_forms/parent_form_js.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["children_form"] = ChildFormset(self.request.POST or None, instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        children_form = context["children_form"]

        with transaction.atomic():
            self.object = form.save()

            if children_form.is_valid():
                children_form.instance = self.object
                children_form.save()

        return HttpResponseRedirect(self.get_success_url())
