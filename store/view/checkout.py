from django.shortcuts import render,redirect
# from .models import Product
from django.views import View
from store.models import Product,Order,OrderedItem,User
# from store.views import Product
from store.templatetags.cart import cart_grand_total


class CheckOut(View):
    def post(self,request):
        print('###### post checkout page')
        name = request.POST.get('name')
        address = request.POST.get('address')
        pin_code = request.POST.get('pin_code')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        phone_2 = request.POST.get('phone_2')
        user = User(id=request.session.get('user_id'))
        cart = request.session.get('cart')                          # not directly used
        # products = request.session.get('cart').keys()
        products = Product.get_products_by_id(list(cart.keys()))    # list of product qs
        # product_ids = list(cart.keys())
        total_item = sum(cart.values())                             # total item count
        product_count = len(cart.values())                          # number of individual product
        grand_total_price = cart_grand_total(products,cart)
        # print(total_item)
        # print(name,address,city,state, phone, phone_2, user, cart, products,product_count,total_item,grand_total_price)
        # for product in products:
        order = Order(
            name = name,
            address = address,
            pin_code = pin_code,
            city = city,
            state = state,
            phone = phone,
            phone_2 = phone_2,
            user = user,
            product_count = product_count,
            total_item = total_item,
            grand_total_price = grand_total_price
        )
        order.place_order()
        print(order)
        #### order items 
        latest_order_id = Order.objects.latest('id').id
        cart_product = cart.keys()
        cart_individual_qty = cart.values()
        # price = cart_grand_total(products|,cart)

        print('order =',latest_order_id)
        for product in products:
            orderitem = OrderedItem(
                order = Order(id = latest_order_id),
                product = Product(id = product.id),
                total_qty = cart.get(str(product.id)),
                price = cart_grand_total(products.filter(id=product.id),cart)
            )
            orderitem.save()
        request.session['cart']={}


        return redirect('stores_ns:cart')

    def get(self,request):
        print('######### get checkout')
        return redirect('stores_ns:home')