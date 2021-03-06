from django.db import models
from decimal import Decimal


# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    brand_abbre = models.CharField(max_length=3, unique=True)
    supplier_name = models.CharField(max_length=30)
    url = models.URLField()  # uses URLValidator

    class Meta:
        ordering = ['brand_name']

    def __str__(self):
        return self.brand_name


# SHOULD AN ABSTRACT ITEM CLASS BE CREATED FOR EXPANDABILITY?
class ItemID(models.Model):
    itemid_brand = models.ForeignKey(Brand, to_field='brand_name', on_delete=models.CASCADE)
    item_id = models.CharField(max_length=30, null=False, unique=True)


class Item(models.Model):
    # REQ: Requires a brand to create an item. Brand entry must be created first
    item_brand = models.ForeignKey(Brand, to_field='brand_name', on_delete=models.CASCADE)
    # when specifying to_field, the field that its pointing to must be specified UNIQUE=True (makes sense)
    item_id = models.ForeignKey(ItemID, to_field='item_id', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=40)
    item_description = models.CharField(max_length=40)
    item_color = models.CharField(max_length=10)
    item_color_code = models.CharField(max_length=3)
    item_season = models.CharField(max_length=3, null=True)
    item_date = models.DateTimeField(null=True)  # Figure out what the users will want to see in terms of dates
    item_category = models.CharField(max_length=40)
    item_subcategory = models.CharField(max_length=40, null=True)

    item_price = models.DecimalField(decimal_places=2, null=False, max_digits=100000000)
    item_current_price = models.DecimalField(decimal_places=2, default=item_price, max_digits=100000000)
    item_on_sale = models.BooleanField(default=False)

    item_sku = models.CharField(max_length=5, unique=True)
    item_size = models.CharField(max_length=2, blank=True)

    item_quantity = models.IntegerField(null=False)  # item quantity overall


    # ADD: item quantity in each store
    # ADD: item location
    # ADD: item to STORE's WEBSITE

    class Meta:
        ordering = [models.F('item_brand').asc(nulls_last=True),
                    models.F('item_name').asc(nulls_last=True)]
        # ORDER BY BRAND, THEN BY PRODUCT NAME. F IS SQL

    # ORDERING IS NOT A FREE OPERATION. EACH FIELD YOU ADD TO THE ORDERING
    # INCURS A COST TO YOUR DATABASE. EACH FOREIGN KEY YOU ADD WILL IMPLICITLY
    # INCLUDE ALL OF ITS DEFAULT ORDERING AS WELL.
    # VIEW DJANGO DOC FOR MORE DETAIL

    def setSalePrice(self, percentage):
        dec_percentage = percentage/100
        self.item_current_price = (self.item_price*(1-dec_percentage))
        self.item_on_sale = True

    def setQuantity(self, q):
        self.item_quantity = q

    # FOR ease of use during testing:
    def __str__(self):
        return str(self.item_brand) + ": " + self.item_name
    # str() because __add__ is not defined so have to cast
