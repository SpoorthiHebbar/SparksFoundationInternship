from django.db import models
from datetime import date

class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True,auto_created=True)
    cust_name = models.CharField(max_length=100)
    cust_email = models.EmailField(max_length=200)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.cust_name


class Transaction(models.Model):
    sender = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='sender_set')
    reciever = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='reciever_set')
    amount = models.FloatField(default=0.0)
    date = models.DateField(default= date.today)