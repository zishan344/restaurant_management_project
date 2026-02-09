from django.db import models

# Create your models here.
class Restaurants(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Restaurant_Name"
    )
    owner_name = models.EmailField(
        max_length=100,
        verbose_name="Email"
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name="Contact_Number"
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
        verbose_name="Delivery_Service_Availability"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created_Time"
    )

    class Meta:
        ordering = ["-created_at"]