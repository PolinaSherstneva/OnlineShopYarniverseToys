from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cart, CartItem
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tovar
from .cart import Cart
from .forms import CartAddProductForm


@login_required
def add_to_cart(request, tovar_id):
    cart_item = Cart.objects.filter(phone_number=request.user.phone_number, tovar=tovar_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(phone_number=request.user.phone_number, tovar=tovar_id)
        messages.success(request, "Item added to your cart.")

    return redirect('cart:cart_detail.html')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_detail")


@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(phone_number=request.user.phone_number)
    total_price = sum(item.quantity * item.product.price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/cart_detail.html", context)


def cart(request):
   cart_items = CartItem.objects.filter(phone_number=request.user.phone_number)
   return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})


@require_POST
def cart_add(request, tovar_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=tovar_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=tovar,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart/detail.html')


def cart_remove(request, product_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=product_id)
    cart.remove(tovar)
    return redirect('cart/detail.html')



# Create your views here.
