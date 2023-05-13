from rest_framework import serializers
from .models import AudioFile

class AudioUploadSerializer(serializers.Serializer):
    class Meta:
        model = AudioFile
        fields = ['audio_file']

    def create(self, validated_data):
        audio_file = validated_data['audio_file']
        instance = AudioFile(audio_file=audio_file)
        instance.save()
        return instance