from django.shortcuts import render
from django.http import HttpResponse
from .pages.musicview import MusicView


def index(request):
    return HttpResponse("Hello, world. You're at the music index.")

def musicview(request):
    musicviewobj = MusicView
    return musicviewobj.index(request)