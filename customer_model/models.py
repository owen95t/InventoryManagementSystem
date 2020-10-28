from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12, null=True)
    email = models.EmailField(null=True)
    # address - add address model?
    customer_id = models.IntegerField(max_length=5, unique=True)

    def getName(self):
        return self.first_name + " " + self.last_name

    # will this work?
    def __str__(self):
        return self.getName()
