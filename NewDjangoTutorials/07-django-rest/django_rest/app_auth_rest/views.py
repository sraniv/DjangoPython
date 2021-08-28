from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def index(request):
    date =datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return Response(data = "Time is "+date, status=status.HTTP_200_OK)





