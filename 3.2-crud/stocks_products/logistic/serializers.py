from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'quantity', 'price', 'product']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):

        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            store = StockProduct.objects.create(stock_id=stock.id, product_id=position['product'].id,
                                                 quantity=position['quantity'], price=position['price'])
            store.save()
        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for position in positions:
            store = StockProduct.objects.update_or_create(stock_id=stock.id, product_id= position['product'].id,
                    defaults={"quantity": position['quantity'], 'price': position['price']})
        return stock
