from rest_framework import serializers
from item_model.models import Brand, Item
from order_model.models import Order, OrderItem
from transfer_model.models import Transfer, TransferItems
from customer_model.models import Customer


# IF SERIALIZING ONLY A SINGLE FIELD, MUST MAKE SURE TO ADD COMMA DUE TO TUPLE REQUIREMENT('FIELDNAMETOSERIALIZE',)
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
        rep = super(ItemSerializer, self).to_representation(instance)
        rep['item_brand'] = instance.item_brand.brand_name

        if instance.item_on_sale:
            rep['item_on_sale'] = "Yes"
        elif not instance.item_on_sale:
            rep['item_on_sale'] = "No"

        return rep


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(OrderSerializer, self).to_representation(instance)

        if instance.order_paid:
            rep['order_paid'] = "Yes"
        elif not instance.order_paid:
            rep['order_paid'] = "No"

        rep['customer'] = instance.customer.getName()

        return rep


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(OrderItemSerializer, self).to_representation(instance)
        rep['order'] = instance.order.order_id
        rep['order_item'] = instance.order_item.item_name

        return rep


class TransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TransferSerializer, self).to_representation(instance)

        if instance.complete_status:
            rep['complete_status'] = "Yes"
        elif not instance.complete_status:
            rep['complete_status'] = "No"

        return rep


class TransferItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransferItems
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TransferItemSerializer, self).to_representation(instance)
        rep['transfer'] = instance.transfer.transfer_id
        rep['transfer_item'] = instance.transfer_item.item_name


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
