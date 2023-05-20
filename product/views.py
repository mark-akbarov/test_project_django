from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        return super(ProductViewSet, self).get_permissions()
    

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    filterset_class = ProductFilter
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60*10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
