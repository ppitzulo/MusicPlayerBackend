from rest_framework import serializers
from .models import AudioFile

class AudioUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['audio_file', 'title', 'runtime', 'thumbnail', 'artist']

    def create(self, validated_data):
        audio_file = validated_data['audio_file']
        instance = AudioFile(audio_file=audio_file)
        instance.save()
        return instance