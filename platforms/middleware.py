from .models import HttpRequestLog


class HttpRequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        HttpRequestLog.objects.create(
            method=request.method,
            path=request.path,
        )

        response = self.get_response(request)

        return response
