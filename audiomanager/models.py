from django.db import models
from datetime import timedelta
import eyed3
import os
from django.conf import settings

# Create your models here.
class AudioFile(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    title = models.CharField(max_length=255, default="Untitled")
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    runtime = models.DurationField(default=timedelta(seconds=0))
    artist = models.CharField(max_length=255, default="Unknown")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       
        if self.audio_file:
            self.title = self.audio_file.name.split('.')[0]
        super().save(*args, **kwargs)
        
        file_path = self.audio_file.path
        audio = eyed3.load(file_path)

        if audio.info is not None:
            # File has been uploaded and the model instance is created

            # Get the file path

            # Extract metadata from the audio file using the file path
            duration_seconds = int(audio.info.time_secs)

            self.runtime = timedelta(seconds=duration_seconds)
            if audio.tag.artist is not None:
                self.artist = audio.tag.artist

            self.thumbnail = extract_thumbnail(file_path)
            # ...

            # Save the model instance with the extracted metadata
            super().save(*args, **kwargs)

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