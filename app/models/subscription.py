from django.db import models

class Subscription(models.Model):
    plan = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()  # Price per month in NTD

    def __str__(self):
        return self.plan