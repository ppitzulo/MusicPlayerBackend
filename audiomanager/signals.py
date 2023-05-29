# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AudioFile
from mutagen import File
from datetime import timedelta
import os
import eyed3
from django.conf import settings

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

        instance.thumbnail = extract_thumbnail(file_path)
        # ...

        # Save the model instance with the extracted metadata
        instance.save()


def extract_thumbnail(audio_file_path):
    audio = eyed3.load(audio_file_path)
    # Convert the filename extension to .jpg
    thumbnail_filename = os.path.basename(audio_file_path).split('.')[0] + '.jpg'
    thumbnail_url = "thumbnails/" + thumbnail_filename
    thumbnail_path = os.path.join(settings.MEDIA_ROOT, "thumbnails/" + thumbnail_filename)

    if audio.tag and audio.tag.images:
        for image in audio.tag.images:
            # Get the image data
            image_data = image.image_data
            # Save the image to a file
            with open(thumbnail_path, "wb") as f:
                f.write(image_data)

            # Exit the loop after finding the first thumbnail
            return thumbnail_url