from django.db import models

# Create your models here.
class AudioFile(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)