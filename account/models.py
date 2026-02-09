from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Restaurant_Name"
    )
    owner_name = models.EmailField(
        max_length=250,
        verbose_name="Email"
    )
    ponoe_number = models.CharField(
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
        verbose_name="delivery_service_availability"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="created_time"
    )

    class Meta:
        ordering = ["-created_at"]