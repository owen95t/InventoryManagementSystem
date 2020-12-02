from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import *
from item_model.models import Brand, Item, ItemID
from order_model.models import Order, OrderItem
from transfer_model.models import Transfer, TransferItems
from customer_model.models import Customer


# Create your views here.

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('brand_name')
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand_name']


class ItemIDViewSet(viewsets.ModelViewSet):
    queryset = ItemID.objects.all().order_by('itemid_brand')
    serializer_class = ItemIDSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['item_id']


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('item_brand__brand_name', 'item_name')
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['item_brand__brand_name', 'item_name', 'item_id__item_id', 'item_name', 'item_sku']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_id', 'customer__first_name', 'customer__last_name']


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['transfer_id']


class TransferItemViewSet(viewsets.ModelViewSet):
    queryset = TransferItems.objects.all()
    serializer_class = TransferItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['transfer__transfer_id']


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('first_name', 'last_name')
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['first_name', 'last_name', 'phone_number']
