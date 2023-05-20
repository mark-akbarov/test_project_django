from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.CharFilter(field_name='price', lookup_expr='gte')
    max_price = filters.CharFilter(field_name='price', lookup_expr='lte')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'name']
