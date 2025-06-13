from playsound import playsound
import os

def playAssistantSound():
    music_dir = os.path.join("www", "assets", "audio", "audio.mp3")
    if os.path.exists(music_dir):
        playsound(music_dir)
    else:
        print("Audio file not found:", music_dir)
