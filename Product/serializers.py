from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Product


class ProductModel:
    def __init__(self, order_id, p_type, p_kind, p_density, p_width, p_format, p_height, created_at, updated_at, file, is_moved):
        self.order_id = order_id
        self.p_type = p_type
        self.p_kind = p_kind
        self.p_density = p_density
        self.p_width = p_width
        self.p_format = p_format
        self.p_height = p_height
        self.created_at = created_at
        self.updated_at = updated_at
        self.file = file
        self.is_moved = is_moved

class ProductSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    p_type = serializers.CharField(max_length=50)
    p_kind = serializers.CharField(max_length=50)
    p_density = serializers.CharField(max_length=50)
    p_width = serializers.CharField(max_length=50)
    p_format = serializers.CharField(max_length=50)
    p_height = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    file = serializers.FileField()
    is_moved = serializers.BooleanField(default=True)

#def encode():
#   model = ProductModel('p_kind : 350', 'p_density', 'p_width', 'p_format', 'p_height', 'created_at', 'updated_at', 'file',  'is_moved')
#    model_sr = ProductSerializer(model)
#    print(model_sr.data, type(model_sr.data), sep='\n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)