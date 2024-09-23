from django.contrib import admin
from .models import Customer, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('customer__first_name', 'customer__last_name')
