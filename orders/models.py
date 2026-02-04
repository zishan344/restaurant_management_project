from django.db import models
from random import choice
# Create your models here.

class OrderStatus(models.Model):
    # Defining choices for order status
    statuses = [
        ('PENDING','pending'),
        ('PROCESSING','processing'),
        ('COMPLETED','completed'),
        ('CANCELLED','cancelled'),
    ]
    name = models.CharField(
        max_length=50,
        unique=True, 
        choices=statuses,
        default='PENDING',
        verbose_name="StatusName")
    # string represent
    def __str__(self):
        return self.name
