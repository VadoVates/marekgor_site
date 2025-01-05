from django.http import HttpResponseForbidden

class BlockSuspiciousPathsMiddleware:
    BLOCKED_PATHS = [
        "/wp-admin/", "/wp-content/", "/wp-includes/", "/.git/",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        for path in self.BLOCKED_PATHS:
            if request.path.startswith(path):
                return HttpResponseForbidden("Forbidden")
        return self.get_response(request)
