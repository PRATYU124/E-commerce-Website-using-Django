from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=1)

    def __str__(self):
        return f"Cart of {self.user.username}"



class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.product.price


    def __str__(self):
        return str(self.user.username) + " "+str(self.total_price)
   
   
@receiver(post_save, sender=CartItems)
def correct_price(sender, **kwargs): 
    cart_items=kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price=cart_items.quantity* float(price_of_product.price)
    total_cart_items = CartItems.objects.filter(user = cart_items.user)
    cart=Cart.objects.get(id=cart_items.cart.id)
    cart.total_price=cart_items.price
    cart.save()



class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount =models.FloatField(default=0)
    is_paid =models.BooleanField(default=False)
    order_id = models.CharField(max_length=100,blank=True)
    payment_id = models.CharField(max_length=100,blank=True)
    payment_signature = models.CharField(max_length=100,blank=True)


class orderedItems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)



