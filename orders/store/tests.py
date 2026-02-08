from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer, Product, Order, OrderItem

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            customer_name="Trisha",
            customer_phoneNo="09171234567",
            customer_address="Cagayan de Oro",
            customer_email="trisha@example.com"
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.customer_name, "Trisha")
        self.assertEqual(str(self.customer), "Trisha")


class CustomerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {
            "customer_name": "Angela",
            "customer_phoneNo": "09179876543",
            "customer_address": "Davao City",
            "customer_email": "angela@example.com"
        }
        self.customer = Customer.objects.create(**self.customer_data)

    def test_get_customers(self):
        response = self.client.get(reverse('customer-list'))  # DRF router naming
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['customer_name'], "Angela")

    def test_create_customer(self):
        new_customer = {
            "customer_name": "Rika",
            "customer_phoneNo": "09171112222",
            "customer_address": "Manila",
            "customer_email": "rika@example.com"
        }
        response = self.client.post(reverse('customer-list'), new_customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    def test_delete_customer(self):
        response = self.client.delete(reverse('customer-detail', args=[self.customer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
