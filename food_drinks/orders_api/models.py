from django.db import models

class Customer(models.Model):
    first_name      = models.CharField(max_length=100)
    middle_name     = models.CharField(max_length=100, null=True, blank=True)
    last_name       = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=15)
    email           = models.EmailField()
    address         = models.CharField(max_length=200)
    photo           = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.email


class Order(models.Model):
    user_code = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_list = models.CharField(max_length =200)
    date_time = models.CharField(max_length =30)

    def __str__(self):
        return self.user_code
    


