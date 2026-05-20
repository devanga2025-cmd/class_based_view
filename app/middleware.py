class RequestInfoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.custom_message = "Request passed through middleware"
        request.user_ip = request.META.get('REMOTE_ADDR')
        request.request_method = request.method

        response = self.get_response(request)

        return response