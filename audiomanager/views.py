from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import AudioUploadSerializer
from .models import AudioFile

class AudioUploadAPIView(APIView):
    def post(self, request):
        serializer = AudioUploadSerializer(data=request.FILES)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'File uploaded successfully'})
        else:
            return Response(serializer.errors, status=400)

class AudioAPIView(ListAPIView):
    queryset = AudioFile.objects.all()
    serializer_class = AudioUploadSerializer
    # queryset = AudioFile.objects.all()
    # serializer_class = AudioUploadSerializer
    # lookup_field = 'pk'

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     obj = queryset.get(pk=self.kwargs['pk'])
    #     return obj