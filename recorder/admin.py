from django.contrib import admin

from .models import AudioMessage

# Register your models here.

class AudioMessageAdmin(admin.ModelAdmin):
    list_display = ('audio_file',)

admin.site.register(AudioMessage, AudioMessageAdmin)
