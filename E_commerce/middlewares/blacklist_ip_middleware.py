from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin

class BlackListIPMiddleware(MiddlewareMixin):
    BLACK_IP_LIST = [
        # 127.0.0.1
        # 
        
    ]

    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))

        if request.META.get('REMOTE_ADDR') in self.BLACK_IP_LIST:
            return PermissionDenied()

    