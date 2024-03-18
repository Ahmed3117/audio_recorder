
from django.http import JsonResponse
from django.shortcuts import render
from .models import AudioMessage
import os
from django.utils import timezone
def record(request):
    return render(request,'recorder/record.html')
    
def store_audio_message(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']  # make sure the name matches the name used in FormData
        filename = 'message_{}.webm'.format(timezone.now().strftime('%Y%m%dT%H%M%S'))
        audio_file.name = filename
        audio_message = AudioMessage(audio_file=audio_file)
        audio_message.save()
        return JsonResponse({'message': 'Saved'})
    else:
        return JsonResponse({'error': 'Not a POST request'})
