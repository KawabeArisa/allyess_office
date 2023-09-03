from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from prograce.models import OrderListData, SupplierData, WorkNameData
from prograce.api.serializers import OLDPostSerializer, SDPostSerializer, WNDPostSerializer

class OrderListDataViewSet(viewsets.ModelViewSet):
    queryset = OrderListData.objects.all()
    serializer_class = OLDPostSerializer

class SupplierDataViewSet(viewsets.ModelViewSet):
    queryset = SupplierData.objects.all()
    serializer_class = SDPostSerializer

class WorkNameDataViewSet(viewsets.ModelViewSet):
    queryset = WorkNameData.objects.all()
    serializer_class = WNDPostSerializer
