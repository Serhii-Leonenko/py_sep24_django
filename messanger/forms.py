from django import forms

from messanger.models import Message


class MessageForm(forms.ModelForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )

    class Meta:
        model = Message
        fields = ("message",)  # Include the hidden 'user' field


# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ("message",)
