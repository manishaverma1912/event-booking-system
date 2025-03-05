from django.db import models


# Create your models here.

class Booking(models.Model):
    name =models.CharField(max_length =25)
    address =models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)


    def __str__(self):
        return self.name

