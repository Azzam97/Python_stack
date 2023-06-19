from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = int(request.POST["id"])
    myproduct = Product.objects.get(id = id_from_form)
    total_charge = quantity_from_form * myproduct.price
    print("Charging credit card...")
    sum_quantity = 0
    sum_charge = 0
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    orders = Order.objects.all()
    for order in orders.values_list():
        sum_quantity = sum_quantity + order[1]
        sum_charge = sum_charge + order[2]
    request.session['quantity'] = int(sum_quantity)
    request.session['total_charge'] = float(sum_charge)
    request.session['recent_charge'] = float(total_charge)
    return redirect('/checkout')


def checkout(request):
    context = {
        'quantity': request.session['quantity'],
        'total_charge': request.session['total_charge'],
        'recent_charge': request.session['recent_charge']
    }
    return render(request, "store/checkout.html", context)
