from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .serializers import AudioUploadSerializer
from .models import AudioFile

class AudioUploadAPIView(APIView):
    def post(self, request):
        if request.method == 'POST':
            files = request.FILES.getlist('files')
            if len(files) == 0:
                return JsonResponse({'error': 'No file was submitted'})
            
            for file in files:
                instance = AudioFile(url=file)
                instance.save()

            return JsonResponse({'message': 'Files uploaded successfully'})
        return JsonResponse({'error': 'Invalid request method'})

class AudioAPIView(ListAPIView):
    queryset = AudioFile.objects.all()
    serializer_class = AudioUploadSerializer

class CSRFTokenAPIView(APIView):
    def get(self, request):
        token = get_token(request)
        return Response({'csrfToken': token})
    
class SearchView(generics.ListCreateAPIView):
    search_fields = ['artist', 'title']
    filter_backends = (filters.SearchFilter,)
    queryset = AudioFile.objects.all()
    serializer_class = AudioUploadSerializer