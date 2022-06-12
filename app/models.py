from django.db import models

# Create your models here.


class SellerRegistration(models.Model):

    acc_name = models.CharField(max_length=120)
    acc_number = models.BigIntegerField()
    branch = models.CharField(max_length=120)
    ifsc = models.BigIntegerField()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    pin = models.IntegerField()
    password = models.CharField(max_length=120)

    class Meta:
        db_table = "sellerreg"


class AdminLogin(models.Model):
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "adminlogin"
