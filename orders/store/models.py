from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phoneNo = models.CharField(max_length=20)
    customer_address = models.TextField()
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_description = models.TextField()

    def __str__(self):
        return self.product_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order {self.id} - {self.customer.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"
