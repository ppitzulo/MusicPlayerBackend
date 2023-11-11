from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse
from .serializers import AudioUploadSerializer
from django.core.paginator import Paginator
from django.db import models
from .models import AudioFile
import os
from django.conf import settings

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

class AudioAPIView(APIView):
    def get(self, request):
        queryset = AudioFile.objects.all()
        paginator = Paginator(queryset, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if page_number and int(page_number) > paginator.num_pages:
            return Response([])

        serializer = AudioUploadSerializer(page_obj, many=True, context={'request': request})

        return Response(serializer.data)

class AudioAPITest(APIView):
    def get(self, request, song_id):

        song = AudioFile.objects.get(id=song_id)
        song_data = song.url.path
        with open(song_data, "rb") as file:
            response = HttpResponse(file.read(), content_type="audio/mpeg")
        return response
        

class CSRFTokenAPIView(APIView):
    def get(self, request):
        token = get_token(request)
        return Response({'csrfToken': token})
    
class SearchView(generics.ListCreateAPIView):
    search_fields = ['artist', 'title']
    filter_backends = (filters.SearchFilter,)
    queryset = AudioFile.objects.all()
    serializer_class = AudioUploadSerializer