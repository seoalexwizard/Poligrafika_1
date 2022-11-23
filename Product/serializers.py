from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('order_id', 'p_type', 'p_kind', 'p_density', 'p_width', 'p_format', 'p_height', 'created_at', 'updated_at', 'file', 'is_moved')