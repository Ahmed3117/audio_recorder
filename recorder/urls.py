from django.urls import path
from . import views

app_name='recorder'

urlpatterns = [
    path('record/', views.record, name='record'),
    path('audio_messages/', views.store_audio_message, name='store_audio_message'),
]

