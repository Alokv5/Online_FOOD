from django import template
from customer.models import CartItemModel
register=template.Library()


@register.simple_tag()
def totalAmount(quantity,price):
    return price*quantity



g_total=0
@register.simple_tag()
def grandTotal(request):
    c_id = request.session['customer_id']
    cart_items = CartItemModel.objects.filter(customer_id=c_id)
    g_total=0
    for x in cart_items:
        g_total=g_total+x.food.price*x.quantity
    # amount=totalAmount(quantity,price)
    # global g_total
    # g_total=g_total+amount
    return g_total





