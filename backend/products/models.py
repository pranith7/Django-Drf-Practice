from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField( max_digits=15, decimal_places=2, default=9.99)

    @property
    def sales_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount_price(self):
        return "12345"


