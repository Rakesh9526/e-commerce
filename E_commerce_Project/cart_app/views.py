from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart,CartIteam
from e_app.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_id(req):
    cart=req.session.session_key
    if not cart:
        cart=req.session.create()
    return cart

def add_cart(req,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(req))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
                cart_id=cart_id(req)
        )
        cart.save(),
    try:
        cart_item=CartIteam.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartIteam.DoesNotExist:
        cart_item=CartIteam.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart_app:cart_detail')

def cart_detail(req,total=0,counter=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=cart_id(req))
        cart_items = CartIteam.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(req,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))


def cart_remove(req,product_id):
    cart=Cart.objects.get(cart_id=cart_id(req))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartIteam.objects.get(product=product,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_detail')

def full_remove(req,product_id):
    cart=Cart.objects.get(cart_id=cart_id(req))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartIteam.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_detail')
