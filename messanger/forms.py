from django import forms

from messanger.models import Message


# class MessageForm(forms.Form):
#     message = forms.CharField()


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("message",)
