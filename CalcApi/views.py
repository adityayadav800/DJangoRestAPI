from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST","GET"])
def calc(request):

    try:
    	if(request.method=='GET'):
    		first_number=int(request.GET.get('value1'))
    		second_number = int(request.GET.get('value2'))
    		operation=request.GET.get('operation')
    		result=0
    		if(operation==' '):
    			result=first_number+second_number
    		if(operation=='-'):
    			result=first_number-second_number
    		if(operation=='*'):
    			result=first_number*second_number
    		return JsonResponse({"result":result})
    	if(request.method=='POST'):
    		first_number=int(request.POST.get('value1'))
    		second_number = int(request.POST.get('value2'))
    		operation=request.POST.get('operation')
    		print()
    		print(type(operation))
    		print(operation)
    		result=0
    		if(operation=='+'):
    			result=first_number+second_number
    		if(operation=='-'):
    			result=first_number-second_number
    		if(operation=='*'):
    			result=first_number*second_number
    		return JsonResponse({"result":result})
    except ValueError as e:
    	return Response(e.args[0],status.HTTP_400_BAD_REQUEST)