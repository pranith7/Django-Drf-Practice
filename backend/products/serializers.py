from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            "title",
            "content",
            "price",
            'sales_price',
            'my_discount'
        ]
    
    def get_my_discount(self,obj):
        try:
            return f"{obj.get_discount_price()}"
        except:
            return None
