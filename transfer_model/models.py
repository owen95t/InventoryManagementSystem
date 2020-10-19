from django.db import models
from item_model.models import Item
import datetime


# Create your models here.

class Transfer(models.Model):
    # Assuming store uses 3 digit store/location code
    transfer_id = models.CharField(max_length=4, unique=True)
    location_to = models.CharField(max_length=3)
    location_from = models.CharField(max_length=3)
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True)

    complete_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created'] # - for descending. Ascending default

    def setCompleted(self):
        # Needs to pass in date object, and assign date object as per above specs
        self.date_completed = datetime.date.today()
        self.complete_status = True

    def __str__(self):
        return self.transfer_id


class TransferItems(models.Model):
    transfer = models.ForeignKey(Transfer, to_field='transfer_id', on_delete=models.CASCADE)
    transfer_item = models.ForeignKey(Item, to_field='item_sku', on_delete=models.CASCADE)
