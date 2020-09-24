from django.shortcuts import render,redirect
from .models import Product
from django.views import View
from django.http import Http404
# from accounts.decorators import unauthenticated_user
# Create your views here.


class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        if 'pdts-minus' in request.POST or 'pdts-add' in request.POST or 'pdts-add-btn' in request.POST:
            return redirect('stores_ns:products')
        else:
            return redirect('stores_ns:home')

    # @unauthenticated_user
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        print("You are :",request.session.get('email'))
        pdts = Product.objects.all()
        return render(request,'store/index.html',{'pdts':pdts})

    # return render(request,'store/index.html',{'pdts':pdts})


def product_page(request):

    pdts = Product.objects.all()
    return render(request,'store/products.html',{'pdts':pdts})


def productdetails_page(request, pk):
    if request.method == 'GET':
        pdts = Product.objects.filter(pk = pk)
        if not pdts:
            raise Http404('Product does not exist')
        return render(request,'store/productdetails.html',{'pdts':pdts})




def cart_page(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('stores_ns:cart')
    else:
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Product.get_products_by_id(ids)       # from models
        return render(request,'store/cart.html',{'products':products})


def aboutus_page(request):
    return render(request,'store/aboutus.html')

def contact_page(request):
    return render(request,'store/contact.html')







def test_page(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)       # from models
    return render(request,'store/test.html',{'products':products})
    # return render(request,'store/test.html')



# from .models import Product,Order,OrderedItem,User
# from .templatetags.cart import cart_grand_total
# def checkout_page(request):
#     if request.method == 'POST':
#         print('###### post checkout page')
#         name = request.POST.get('name')
#         address = request.POST.get('address')
#         pin_code = request.POST.get('pin_code')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         phone = request.POST.get('phone')
#         phone_2 = request.POST.get('phone_2')
#         user = User(id=request.session.get('user_id'))
#         cart = request.session.get('cart')                          # not directly used
#         # products = request.session.get('cart').keys()
#         products = Product.get_products_by_id(list(cart.keys()))    # list of product qs
#         # product_ids = list(cart.keys())
#         total_item = sum(cart.values())                             # total item count
#         product_count = len(cart.values())                          # number of individual product
#         grand_total_price = cart_grand_total(products,cart)
#         # print(total_item)
#         # print(name,address,city,state, phone, phone_2, user, cart, products,product_count,total_item,grand_total_price)
#         # for product in products:
#         order = Order(
#             name = name,
#             address = address,
#             pin_code = pin_code,
#             city = city,
#             state = state,
#             phone = phone,
#             phone_2 = phone_2,
#             user = user,
#             product_count = product_count,
#             total_item = total_item,
#             grand_total_price = grand_total_price
#         )
#         order.place_order()
#         print(order)
#         #### order items 
#         latest_order_id = Order.objects.latest('id').id
#         cart_product = cart.keys()
#         cart_individual_qty = cart.values()
#         # price = cart_grand_total(products|,cart)

#         print('order =',latest_order_id)
#         for product in products:
#             orderitem = OrderedItem(
#                 order = Order(id = latest_order_id),
#                 product = Product(id = product.id),
#                 total_qty = cart.get(str(product.id)),
#                 price = cart_grand_total(products.filter(id=product.id),cart)
#             )
#             orderitem.save()
#         request.session['cart']={}


#         return redirect('stores_ns:cart')

#     else:
#         print('######### get checkout')
#         return redirect('stores_ns:home')