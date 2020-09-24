from django.db import models
from django.utils import timezone
from store.models import Order
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User

# Create your models here.




class OrderStack(models.Model):
  order_fk = models.ForeignKey(Order, on_delete=models.CASCADE)
  order_time = models.DateTimeField(default = timezone.now)
  last_status = models.CharField(max_length=50, blank=True, null=True)
  status_time = models.DateTimeField(default = timezone.now)
  active = models.BooleanField(default=True)
  updated_by = models.CharField(max_length=70, blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  # def __str__(self):
  #     return self.user.email
  def order_id(self):
    return self.id

  def user_name(self):
    return self.order_id.user.email

  @staticmethod
  def active_order():
    return OrderStack.objects.filter(active=True)


  # @staticmethod
  # def get_order_manage_by_user(user):
  #   return Order.objects.filter(user=user)
@receiver(post_save,sender=Order)
def create_order_stack(sender,instance,created,**kwargs):
  if created:
    user_email = User.objects.get(id=instance.user_id).email
    OrderStack.objects.create(order_fk=instance,last_status='Order Placed',updated_by=user_email)
    print('## Order Stack Created')


@receiver(post_save,sender=Order)
def update_order_stack(sender,instance,created,**kwargs): 
  if not created:
    instance.order.save()
    print('## Order Stack Updated')