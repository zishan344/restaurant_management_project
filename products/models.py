from django.db import models
from account.models import Restaurant
# Create your models here.
class MenuItem(models.Model):
    ''' restaurant menu item '''
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant"
        verbose_name="restaurant"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="item_name"
        )
    description = models.TextField(
        null = True, 

    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="price"
        ),
    is_available = models.BooleanField(
        default = True,
        verbose_name="available_item"
    ),
    is_featured = models.BooleanField(
        default=False,
        verbose_name="featured_item"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)