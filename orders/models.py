from django.db import models
# Create your models here.

class OrderStatus(models.Model):
    # Defining choices for order status
    STATUSES = [
        ('PENDING','pending'),
        ('PROCESSING','processing'),
        ('COMPLETED','completed'),
        ('CANCELED','canceled'),
    ]
    name = models.CharField(
        max_length=50,
        unique=True,
        choices=STATUSES,
        default='PENDING',
        verbose_name="Status Name"
    )
    # string represent
    def __str__(self):
        return self.name