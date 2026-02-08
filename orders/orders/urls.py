from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import (
    CustomerViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet,
    customer_page, product_page, order_page, order_item_page
)
from django.shortcuts import redirect

# ===========================
# REST API router
# ===========================
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

# ===========================
# Root redirect
# ===========================
def root_redirect(request):
    return redirect('customers')  # Redirect root to customers page

# ===========================
# URL patterns
# ===========================
urlpatterns = [
    path('', root_redirect),  # root URL
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Business UI (Template Views)
    path('customers-page/', customer_page, name="customers"),
    path('products-page/', product_page, name="products"),
    path('orders-page/', order_page, name="orders"),
    path('order-items-page/', order_item_page, name="order_items"),
]
