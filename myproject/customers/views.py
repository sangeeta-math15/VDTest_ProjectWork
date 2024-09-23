from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from rest_framework import status


class TopCustomersView(APIView):
    def get(self, request):
        try:
            top_customers = Order.top_customers()

            response_data = []

            for customer in top_customers:
                customer_id = customer.get('customer__id', None)
                first_name = customer.get('customer__first_name', '')
                last_name = customer.get('customer__last_name', '')
                total_spent = customer.get('total_spent', 0.00)

                response_data.append({
                    'customer_id': customer_id,
                    'full_name': f"{first_name} {last_name}",
                    'total_spent': total_spent,
                })

            if not response_data:
                return Response(
                    {"message": "No customers found in the last 6 months."},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "An error occurred while fetching top customers.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
