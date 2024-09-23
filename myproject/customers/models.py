from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cust_orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.customer.full_name} - ${self.total_amount}"

    @classmethod
    def top_customers(cls):
        six_months_ago = timezone.now() - timezone.timedelta(days=180)
        print(six_months_ago)
        return (
            cls.objects.filter(order_date__gte=six_months_ago, status='completed')
            .values('customer__id', 'customer__first_name', 'customer__last_name')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
