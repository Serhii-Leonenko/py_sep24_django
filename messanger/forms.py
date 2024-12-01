from django import forms

from messanger.models import Message

from django.contrib.auth import get_user_model

User = get_user_model()


class MessageForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput(),
        queryset=User.objects.all(),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )

    class Meta:
        model = Message
        fields = ("message", "user")


# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ("message",)
