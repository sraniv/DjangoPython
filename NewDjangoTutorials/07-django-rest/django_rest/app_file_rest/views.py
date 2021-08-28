from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


#####################################################################################
@api_view(['GET', 'POST', 'PUT'])
def random_number(request):
    from random import randint

    if request.method == "GET":
        return Response({"GETdata": randint(0, 100)}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response({"POSTdata": randint(0, 100)}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        return Response({"PUTdata": randint(0, 100)}, status=status.HTTP_200_OK)
    else:
        data = {"Error": {"status": 400,"message": "Request Error"}}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


#####################################################################################
def evenodd(n1):
    if n1%2 == 0:
        return {n1:'EVEN'}
    else:
        return {n1:'ODD'}

@api_view(['GET', 'POST'])
def even_odd(request):
    
    if request.method == 'GET': # and 'N1' in request.GET:
        #
        #######################
        # Read Body Variables
        #######################
        # request.GET is the body parameter dictionary
        data = request.GET['N1']
        return Response(evenodd(int(data)), status=status.HTTP_200_OK)
    #    
    elif request.method == 'POST': # and 'N1' in request.POST:
    
        #######################
        # Read Body Variables
        #######################
        # request.POST is the parameter dictionary        
        data = request.POST['N1']
        return Response(evenodd(int(data)), status=status.HTTP_200_OK)
    #
    else:
        data = {"Error": {"status": 400,
                          "message": "Expected N1 Integer Parameter"}}

        return Response(data, status=status.HTTP_400_BAD_REQUEST)


#####################################################################################
@api_view(['GET', 'POST'])
def get_custom_header(request):

    if request.method == "GET":
        #
        #######################
        # Read Header Variables
        #######################
        l_header_prefix = 'HTTP_'
        # Header Parameter Dictionary
        H1 = request.META[l_header_prefix+'H1']

        l_return = {"GET Custom Header Data H1":H1}
        return Response(l_return, status=status.HTTP_200_OK)
    #
    elif request.method == "POST":
        #
        #######################
        # Read Header Variables
        #######################
        l_header_prefix = 'HTTP_'
        # Header Parameter Dictionary
        H1 = request.META[l_header_prefix+'H1']

        l_return = {"POST Custom Header Data H1":H1}
        return Response(l_return, status=status.HTTP_200_OK)
    #
    else:
        data = {"Error": {"status": 400,
                          "message": "Request Error"}}

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

