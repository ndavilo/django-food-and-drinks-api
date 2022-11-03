from django.shortcuts import render
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
