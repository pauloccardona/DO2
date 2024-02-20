from rest_framework import serializers

from pizzaria.function import attemp_json_deserialize
from pizzaria.models import Waitress, Order, Pizza, Topping

class WaitressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitress
        fields = ('id', 'name')

class OrderSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= ('id', 'customer', 'address')

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Topping
        fields= ('name')

class PizzaSerializer(serializers.ModelSerializer):
    order= OrderSummarySerializser(read_only= True)
    waitress= WaitressSerializer(read_only= True)
    toppings= ToppingSerializer(read_only= True, many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'order', 'waitress', 'toppings')

    def update(self, instance, validated_data):
        request = self.context['request']

        order_data = request_data.get('order')
        order_data = attemp_json_deserialize(order_data, expect_type=str)
        validated_data['order_id'] = order_data

        waitress_data = request.data.get('waitress')
        waitress_data = attemp_json_deserialize(waitress_data, expect_type=dict)
        waitress = Waitress.objects.create(**waitress_data)
        validated_data['waitress'] = waitress

        toppings_data = request.data.get('toppings')
        toppings_ids = attemp_json_deserialize(toppings_data, expect_type=list)
        validated_data['toppings'] = toppings_ids

        instance = super().update(instance, validated_data)

        return instance

class PizzaSummarySerializer(serializers.ModelSerializer):
    waitress = WaitressSerializer(read_only=True)

    class Meta:
        model = Pizza
        fields = ('id', 'waitress', 'toppings')

class OrderDetailSerializer(serializers.ModelSerializer):
    pizzas = PizzaSummarySerializer(read_only=True, many=True)

    class Meta:
        Model = Order
        fields = ('id', 'customer', 'address', 'pizzas')




