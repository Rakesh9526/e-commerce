from . models import Cart,CartIteam
from .views import cart_id


def counter(req):
    item_count=0
    if 'admin' in req.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cart_id(req))
            cart_items=CartIteam.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)
