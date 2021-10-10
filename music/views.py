from django.shortcuts import render
from django.http import HttpResponse
from .pages.musicview import MusicView
from .models import MusicButton


def index(request):
    return HttpResponse("Hello, world. You're at the music index.")

def musicview(request):
    musicviewobj = MusicView
    return musicviewobj.index(request)

def play(request):
    music_button = MusicButton('./sounds/piano-a.wav', 'A')
    music_button.play_sound()
    return request