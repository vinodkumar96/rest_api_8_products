from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

# Create your views here.
def input(request):
    return render(request,'input.html')
def link(request):
    p_id1 = int(request.POST['t1'])
    p_name1 = request.POST['t2']
    p_cost1 = float(request.POST['t3'])
    p_mfd1 = request.POST['t4']
    p_exd1 = request.POST['t5']
    f =Product(p_id=p_id1,p_name=p_name1,p_cost=p_cost1,p_mfd=p_mfd1,p_exd=p_exd1)
    f.save()
    return render(request,'link.html')
def display(request):
    recs = Product.objects.all()
    return render(request,'display.html',{'recs':recs})

class ProductList(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serial = ProductSerializer(products,many=True)
        return Response(serial.data)
    def post(self,request,format=None):
        serial = ProductSerializer(data=request.POST)
        if serial.is_valid():
            serial.save()
            return  Response(serial.data)
        return Response(serial.errors)
def inputid(request):
    return render(request, 'input_id.html')
class ProductDetail(APIView):
    def get(self,request,format=None):
        pid1 = int(request.GET['pid'])
        prod = Product.objects.filter(p_id=pid1)
        prod.delete()
        serial = ProductSerializer(prod,many=True)
        return  Response(serial.data)
