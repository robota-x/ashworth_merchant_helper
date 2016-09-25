from django.db import models


class Transaction(models.Model):
    amount = models.FloatField()
    method = models.CharField(max_length=255)
    transaction_fee = models.FloatField()
    time = models.DateTimeField(auto_now=True)