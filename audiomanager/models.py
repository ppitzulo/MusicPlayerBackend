from django.db import models
from datetime import timedelta
from django.conf import settings
import datetime
import eyed3
import os

# Create your models here.
class AudioFile(models.Model):
    url = models.FileField(upload_to='audio/')
    title = models.CharField(max_length=255, default="Untitled")
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    runtime = models.CharField(max_length=10, default="0:00")
    artist = models.CharField(max_length=255, default="Unknown")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       
        if self.url:
            self.title = self.url.name.split('.')[0]
        super().save(*args, **kwargs)
        
        # Get the file path
        file_path = self.url.path
        audio = eyed3.load(file_path)

        if audio.info is not None:
            # Extract metadata from the audio file using the file path
            self.runtime = self.format_runtime(int(audio.info.time_secs))
            if audio.tag.artist is not None:
                self.artist = audio.tag.artist

            self.thumbnail = extract_thumbnail(file_path)

            super().save(*args, **kwargs)
            
    def format_runtime(self, runtime):
        # Takes runtime in seconds and converts to H:M:S or M:S if less than an hour
        
        hours, remainder = divmod(runtime, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(minutes)

        if hours > 0:
            return f'{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'
        else:
            return f'{minutes}:{str(seconds).zfill(2)}'

def extract_thumbnail(audio_file_path):
    audio = eyed3.load(audio_file_path)
    # Convert the filename extension to .jpg
    thumbnail_filename = os.path.basename(audio_file_path).split('.')[0] + '.jpg'
    thumbnail_url = "thumbnails/" + thumbnail_filename
    thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail_url)

    # Create the thumbnails directory if it doesn't exist
    os.makedirs(os.path.join(settings.MEDIA_ROOT, "thumbnails"), exist_ok=True)

    # Check if the audio file has a thumbnail
    if audio.tag and audio.tag.images:
        for image in audio.tag.images:
            image_data = image.image_data
            with open(thumbnail_path, "wb") as f:
                f.write(image_data)

            # Exit the loop after finding the first thumbnail
            return thumbnail_url

