from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import File
from .serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (AllowAny,)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class DownloadAPIView(APIView):
    def get(self, request, file_id):
        file_obj = get_object_or_404(File, id=file_id)
        file_path = file_obj.file.path
        file_response = FileResponse(open(file_path, 'rb'))
        file_response['Content-Disposition'] = f'attachment; filename="{file_obj.name}"'
        return Response({"message": "successfully downloaded"}, status=200, headers={'Content-Disposition': file_response['Content-Disposition']}, content_type='application/json')