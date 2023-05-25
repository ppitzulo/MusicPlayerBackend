# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AudioFile
from mutagen import File
from datetime import timedelta

@receiver(post_save, sender=AudioFile)
def extract_metadata(sender, instance, created, **kwargs):
    if created:
        # File has been uploaded and the model instance is created

        # Get the file path
        file_path = instance.audio_file.path
        audio = File(file_path)

        # Extract metadata from the audio file using the file path
        # if 'length' in audio:
        duration_seconds = int(audio.info.length)

        instance.runtime = timedelta(seconds=duration_seconds)
        if 'artist' in audio:
            instance.artist = audio['artist'][0]
        # ...

        # Save the model instance with the extracted metadata
        instance.save()
