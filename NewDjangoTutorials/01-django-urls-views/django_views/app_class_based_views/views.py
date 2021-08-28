from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse

class DataView(View):

    l_response_data = {"data":"Message from Class Based View"}

    def get(self, request):
        return JsonResponse(self.l_response_data)

    def post(self, request):
        return JsonResponse(self.l_response_data)

    def put(self, request):
        return JsonResponse(self.l_response_data)
