
from django.urls import path
from .views import TopCustomersView

urlpatterns = [
    path('api/top-customers/', TopCustomersView.as_view(), name='top_customers'),
]
