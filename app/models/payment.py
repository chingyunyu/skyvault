from django.db import models

class Payment(models.Model):
    email = models.EmailField()
    plan = models.CharField(max_length=50)
    price = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.email} - {self.plan}"