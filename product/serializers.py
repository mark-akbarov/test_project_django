from rest_framework import serializers
from file.serializers import FileUrlSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image']
        
    def to_representation(self, instance):
        self.fields['image'] = FileUrlSerializer()
        return super(ProductSerializer, self).to_representation(instance)
