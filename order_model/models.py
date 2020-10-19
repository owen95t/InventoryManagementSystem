from django.db import models
from item_model.models import Item
from customer_model.models import Customer


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, to_field='customer_id', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=5, unique=True)
    order_date = models.DateField()
    order_fulfilled = models.BooleanField(default=False)
    order_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    order = models.ForeignKey(Order, to_field='order_id', on_delete=models.CASCADE)
    order_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# The field on the related object that the relation is to.
# By default, Django uses the primary key of the related object.
# If you reference a different field, that field must have unique=True.
