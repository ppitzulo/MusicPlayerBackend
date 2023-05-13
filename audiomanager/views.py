from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .serializers import AudioUploadSerializer
import os

class AudioUploadAPIView(APIView):
    def post(self, request):
        serializer = AudioUploadSerializer(data=request.data)

        if serializer.is_valid():
            # audio_file = serializer.validated_data['audio_file']
            # filename = audio_file.name
            # file_path = os.path.join(settings.MEDIA_ROOT, filename)
            

            # with open(file_path, 'wb') as destination:
            #     for chunk in audio_file.chunks():
            #         destination.write(chunk)
            serializer.save()
            # Process the uploaded file as needed
            # Return a response indicating success or failure
            return Response({'message': 'File uploaded successfully'})
        else:
            return Response(serializer.errors, status=400)
