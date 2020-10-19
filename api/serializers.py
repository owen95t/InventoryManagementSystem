from rest_framework import serializers
from item_model.models import Brand, Item
from order_model.models import Order, OrderItem
from transfer_model.models import Transfer, TransferItems
from customer_model.models import Customer


#IF SERIALIZING ONLY A SINGLE FIELD, MUST MAKE SURE TO ADD COMMA DUE TO TUPLE REQUIREMENT('FIELDNAMETOSERIALIZE',)
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    # to show name when serialized instead of an api link
    def to_representation(self, instance):
        rep = super(BrandSerializer, self).to_representation(instance)
        rep['item_brand'] = instance.item_brand.brand_name
        return rep


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class TransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'


class TransferItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransferItems
        fields = '__all__'


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
