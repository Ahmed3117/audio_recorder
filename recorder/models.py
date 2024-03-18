from django.db import models

# Create your models here.

class AudioMessage(models.Model):
    audio_file = models.FileField(upload_to='audio_messages/')
    
    