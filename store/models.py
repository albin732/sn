from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200,null=False)
    image = models.ImageField(upload_to='image/product',null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    drink = models.BooleanField(default=False)
    # if drink== False:
    size = models.CharField(max_length=20,null=True,blank=True)
    # else:
    #     P_CHOICES = (
    #         ('F', 'Full'),
    #         ('H', 'Half'),
    #         ('Q', 'Quater'),
    #     )
    #     size = models.CharField(max_length=20, choices=P_CHOICES,null=True,blank=True)
    calories = models.CharField(max_length=10,null=True,blank=True)
    category = models.CharField(max_length=30,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    veg = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name

    def __int__(self):
        return self.id

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))

    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    @staticmethod
    def get_products_by_id(ids):
      return Product.objects.filter(id__in=ids)

    
    


User = get_user_model()
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_count = models.IntegerField(default=1)
    total_item = models.IntegerField(default=1)
    grand_total_price = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    tax_total = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    name = models.CharField(max_length=200, blank=True, null=True,default='Name')
    address = models.TextField(blank = True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True, null=True)  # null = True means not mandatory
    phone_2 = models.CharField(max_length=15,blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default = timezone.now)

    # def __str__(self):
    #     return self.user.email

    def place_order(self):
        self.save()

    def order_id(self):
      return self.id

    def user_name(self):
      return self.user.email

    @staticmethod
    def get_order_by_user(user):
      return Order.objects.filter(user=user)


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    total_qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.product.name

    def order_item_id(self):
      return self.id

    def order_id(self):
      return self.order.id

    # def product_name(self):
    #   return self.product.name


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    net_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    PY_METHOD = (
        ('DC', 'Debit Card'),
        ('NB', 'Net Banking'),
        ('PYPL', 'PayPal'),
        ('PHPE', 'PhonePe'),
        ('PYTM', 'Paytm'),
    )
    payment_method = models.CharField(max_length=30, choices=PY_METHOD,null=True,blank=True)
    PY_STATUS = (
        ('PG', 'Pending'),
        ('PD', 'Paid'),
        ('F', 'Failed'),
    )
    payment_status = models.CharField(max_length=30, choices=PY_STATUS,null=True,blank=True)
    remarks = models.CharField(max_length=255,null=True,blank=True,default='success')
    timestamp = models.DateTimeField(auto_now_add=True)

    def payment_id(self):
      return self.id

    def user_name(self):
      return self.order.user.email

    def order_id(self):
      return self.order.id



class Refund(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    net_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    RF_METHOD = (
        ('DC', 'Debit Card'),
        ('NB', 'Net Banking'),
        ('PYPL', 'PayPal'),
        ('PHPE', 'PhonePe'),
        ('PYTM', 'Paytm'),
    )
    refund_method = models.CharField(max_length=30, choices=RF_METHOD)
    PY_STATUS = (
        ('PG', 'Pending'),
        ('F', 'Failed'),
        ('C', 'Canceled'),
        ('RF', 'Refund Initiated'),
        ('RC', 'Refund Completed'),
    )
    refund_status = models.CharField(max_length=30, choices=PY_STATUS)
    remarks = models.CharField(max_length=255,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__ (self):
    #   return self.payment.order.user.email

    # def user_name(self):
    #   return self.order.user.email

    def payment_id(self):
      return self.payment.id

    def order_id(self):
      return self.order.id


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    DY_STATUS = (
        ('UPG', 'Under Processing'),
        ('RFD', 'Ready for Delivery'),
        ('OFD', 'Out for delivery'),
        ('CBU', 'Canceled by User'),
        ('C', 'Canceled'),
        ('R', 'Returned'),
        ('D', 'Delivered'),
    )
    delivery_status = models.CharField(max_length=30, choices=DY_STATUS)
    remarks = models.CharField(max_length=255,null=True,blank=True)
    # Expected_Delivery = models.DateTimeField(default=datetime.now()+timedelta(hours=2))
    Expected_Delivery = models.CharField(max_length=255,null=True,blank=True)
    shipped_by = models.CharField(max_length=100,null=True,blank=True)
    shipped_through = models.CharField(max_length=100,null=True,blank=True)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


    def order_id(self):
      return self.order.id


