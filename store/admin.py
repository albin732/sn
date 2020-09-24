from django.contrib import admin

from .models import Product,Order,OrderedItem,Payment,Refund,Delivery

# Register your models here.


#  product display in admin 
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','image_tag','drink','size','calories','category','veg','special','active','price','gst','timestamp')

    search_fields = ('name',)


#  order display in admin 
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','user_name','product_count','grand_total_price','active','timestamp')

    # search_fields = ('',)


#  ordered Items display in admin 
class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ('order_item_id','order_id','total_qty','price','active')
    
    search_fields = ('order__id',)



#  ordered Items display in admin 
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user_name','payment_id','order_id','net_price','payment_method','payment_status','remarks','timestamp')
    
    search_fields = ('order__user__email',)



#  ordered Items display in admin 
class RefundAdmin(admin.ModelAdmin):
    list_display = ('order_id','payment_id','net_price','refund_method','refund_status','timestamp')

    search_fields = ('order__id',)


#  ordered Items display in admin 
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order_id','delivery_status','remarks','Expected_Delivery','shipped_by','shipped_through','timestamp')

    search_fields = ('order__id',)




admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Refund, RefundAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(OrderedItem, OrderedItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)



