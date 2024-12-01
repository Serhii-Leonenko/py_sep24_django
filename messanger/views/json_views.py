from django.http import JsonResponse

from messanger.models import Message


def json_message_list(request):
    messages = list(Message.objects.values("id", "message"))

    return JsonResponse(messages, safe=False)
