from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        # fields = ('ticker', 'volume') - shows only the ticker and volume fields
