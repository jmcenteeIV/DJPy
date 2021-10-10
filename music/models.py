from django.db import models
from playsound import playsound

# Create your models here.

class MusicButton:
    def __init__(self, file, name) -> None:
        super().__init__()
        self.name = name
        self.note = file
    
    def play_note(self):
        playsound(self.note)
        
