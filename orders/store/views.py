from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Customer, Product, Order, OrderItem
from .serializer import CustomerSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer

# ===========================
# API VIEWSETS (FULL CRUD)
# ===========================

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# ===========================
# TEMPLATE VIEWS
# ===========================

def customer_page(request):
    if request.method == "POST":
        Customer.objects.create(
            customer_name=request.POST.get("name"),
            customer_phoneNo=request.POST.get("phone"),
            customer_address=request.POST.get("address"),
            customer_email=request.POST.get("email"),
        )
        return redirect("customers")
    customers = Customer.objects.all()
    return render(request, "store/customers.html", {"customers": customers})

def product_page(request):
    products = Product.objects.all()
    return render(request, "store/products.html", {"products": products})

def order_page(request):
    orders = Order.objects.all()
    return render(request, "store/orders.html", {"orders": orders})

def order_item_page(request):
    order_items = OrderItem.objects.all()
    return render(request, "store/order_items.html", {"order_items": order_items})
