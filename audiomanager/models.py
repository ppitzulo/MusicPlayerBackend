from django.db import models
from datetime import timedelta

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