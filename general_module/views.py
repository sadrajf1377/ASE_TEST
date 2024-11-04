from decimal import Decimal

from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
import math




# Create your views here.

class Get_Sin(APIView):
    def get(self,request,value):
        value=float(value)
        radian=(3.14/180)*value
        response={'result': math.sin(radian),'message':f'sin({value}) ={math.sin(radian)}'}
        return Response(response,status=200)


class Get_Cos(APIView):
    def get(self,request,value):
        value=float(value)
        radian = (3.14 / 180) * value
        response={'result':math.cos(radian),'message':f'cos({value}) ={math.cos(radian)}'}
        return Response(response,status=200)

class Get_Tan(APIView):
    def get(self,request,value):
        value = float(value)
        radian = (3.14 / 180) * value
        response = {'result': math.tan(radian),'message':f'tan({value}) ={math.tan(radian)}'}
        return Response(response, status=200)

class Get_Cot(APIView):
    def get(self,request,value):
        value = float(value)
        radian = (3.14 / 180) * value
        response = {'result': math.tan(radian)**-1,'message':f'cot({value}) ={math.tan(radian)**-1}'}
        return Response(response, status=200)
