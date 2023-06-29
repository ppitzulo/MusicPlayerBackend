from rest_framework import serializers
from .models import AudioFile

class AudioUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['url', 'title', 'runtime', 'thumbnail', 'artist']