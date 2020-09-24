from django import template

register= template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if  int(id) == product.id:
            return True

    return False 


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if  int(id) == product.id:
            return cart.get(id)

    return 0 


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price*cart_quantity(product,cart)



@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum_price = 0
    for p in products:
        sum_price += price_total(p,cart)

    return sum_price



@register.filter(name='total_cart_gst')
def total_cart_gst(products,cart):
    sum_gst = 0
    for p in products:
        gst = (price_total(p,cart)*p.gst)/100
        sum_gst += gst

    # print(sum_gst+sum_price)
    return sum_gst


@register.filter(name='cart_grand_total')
def cart_grand_total(products,cart):
    sum_price = 0
    sum_gst = 0
    for p in products:
        sum_price += price_total(p,cart)
        gst = (price_total(p,cart)*p.gst)/100
        sum_gst += gst

    return sum_gst+sum_price
    # return 0