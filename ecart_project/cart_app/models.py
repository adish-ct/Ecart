from django.db import models
from ecart_app.models import Product


# Create your models here.

# Table 1 for cart id

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


# Table 2 cart items

class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Cart_Item'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

