from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet, DownloadAPIView


router = DefaultRouter()
router.register('', FileViewSet, 'files')

urlpatterns = [
    path('', include(router.urls)),
    path('download/<int:file_id>/', DownloadAPIView.as_view(), name='file_download'),
]
