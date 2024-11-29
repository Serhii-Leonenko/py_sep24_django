from django.urls import path

from nested_forms.views import (ParentCreateView, ParentListView,
                                ParentUpdateView)

app_name = "nested_forms"

urlpatterns = [
    path("parents/", ParentListView.as_view(), name="parent-list"),
    path("parents/create/", ParentCreateView.as_view(), name="parent-create"),
    path("parents/<int:pk>/update/", ParentUpdateView.as_view(), name="parent-update"),
]
