from urllib import response
from django.utils.deprecation import MiddlewareMixin


class RequestLogMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):

        response = self.get_response(request)

        return response
    def extract_log_info(self,request,view_fun,view_args,view_kvargs):
        pass
    

