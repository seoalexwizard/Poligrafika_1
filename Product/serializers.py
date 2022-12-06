from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Product


#class ProductModel:
#    def __init__(self, order_id, p_type, p_kind, p_density, p_width, p_format, p_height, created_at, updated_at, file, is_moved):
#        self.order_id = order_id
#        self.p_type = p_type
#        self.p_kind = p_kind
#        self.p_density = p_density
#        self.p_width = p_width
#        self.p_format = p_format
#        self.p_height = p_height
#        self.created_at = created_at
#        self.updated_at = updated_at
#        self.file = file
#        self.is_moved = is_moved

class ProductSerializer(serializers.ModelSerializer):
    order_id = serializers.StringRelatedField()
    p_type = serializers.StringRelatedField()
    p_kind = serializers.StringRelatedField()
    p_density = serializers.StringRelatedField()
    p_width = serializers.StringRelatedField()
    p_format = serializers.StringRelatedField()
    p_height = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    updated_at = serializers.StringRelatedField()
    file = serializers.StringRelatedField()
    is_moved = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'
        # order_id = serializers.IntegerField()
        # p_type = serializers.CharField(max_length=50)
        # p_kind = serializers.CharField(max_length=50)
        # p_density = serializers.CharField(max_length=50)
        # p_width = serializers.CharField(max_length=50)
        # p_format = serializers.CharField(max_length=50)
        # p_height = serializers.CharField(max_length=50)
        # created_at = serializers.DateTimeField(read_only=True)
        # updated_at = serializers.DateTimeField(read_only=True)
        # file = serializers.FileField()
        # is_moved = serializers.BooleanField(default=True)

#    def create(self, validated_data):
#        return  Product.objects.create(**validated_data)

#    def update(self, instance, validated_data):
#        instance.order_id = validated_data.get('order_id', instance.order_id)
#        instance.p_type = validated_data.get('p_type', instance.p_type)
#        instance.p_kind = validated_data.get('p_kind', instance.p_kind)
#        instance.p_density = validated_data.get('p_density', instance.p_density)
#        instance.p_width = validated_data.get('p_width', instance.p_width)
#        instance.p_format = validated_data.get('p_format', instance.p_format)
#        instance.p_height = validated_data.get('p_height', instance.p_height)
#        instance.created_at = validated_data.get('created_at', instance.created_at)
#        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
#        instance.file = validated_data.get('file', instance.file)
#        instance.is_moved = validated_data.get('is_moved', instance.is_moved)
#        instance.save()
#        return instance
#def encode():
#   model = ProductModel('p_kind : 350', 'p_density', 'p_width', 'p_format', 'p_height', 'created_at', 'updated_at', 'file',  'is_moved')
#    model_sr = ProductSerializer(model)
#    print(model_sr.data, type(model_sr.data), sep='\n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)