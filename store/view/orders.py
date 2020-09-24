from django.shortcuts import render,redirect
from django.views import View
from store.models import Order
# from store.views import Product
# from store.templatetags.cart import cart_grand_total


class Orders(View):
    def post(self,request):
        user = request.session.get('user_id')
        orders = Order.get_order_by_user(user)
        return render(request,'store/order.html',{'orders':orders})

    def get(self,request):
        user = request.session.get('user_id')
        orders = Order.get_order_by_user(user)
        return render(request,'store/order.html',{'orders':orders})

