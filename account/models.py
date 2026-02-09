from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Restaurant Name"
        )
    owner_name = models.CharField(
        max_length=100,
        verbose_name="Owner Name"
        )
    email = models.EmailField(
        max_length=150,
        verbose_name="Email"
        )

    phone_number = models.CharField(
        max_length=50,
        verbose_name="Contact Number"
        )
    address = models.TextField(
        verbose_name="Address"
        )
    city = models.CharField(
        max_length=100,
        verbose_name="City"
        )
    has_delivery = models.BooleanField(
        default=True,
        verbose_name="Has Delivery"
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
        )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name
