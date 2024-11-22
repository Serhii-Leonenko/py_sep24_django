from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    print("logic before request in simple middleware")
    response = self.get_response(request)
    print("after response")

    return response


class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("logic before request in custom middleware")

    def process_response(self, request, response):
        print("after response")

        return response
