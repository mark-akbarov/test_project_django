from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListAPIView


router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product_list/', ProductListAPIView.as_view(),)
]
