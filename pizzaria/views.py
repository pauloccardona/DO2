from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from pizzaria.models import Waitress, Order, Pizza, Topping
from pizzaria.serializers import(
    OrderSummarySerializer,
    OrderDetailSerializer,
    PizzaSerializer,
    ToppingSerializer
)

class ToppingViewSet(ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return OrderSummarySerializer
        return OrderDetailSerializer