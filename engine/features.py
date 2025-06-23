from playsound import playsound
import os
import eel 
from engine.command import speak
import pywhatkit as kit
from engine.config import ASSISTANT_NAME

@eel.expose
def playAssistantSound():
    music_dir = os.path.join("www", "assets", "audio", "audio.mp3")
    if os.path.exists(music_dir):
        playsound(music_dir)
    else:
        print("Audio file not found:", music_dir)


def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    quer=query.replace("open","")
    query.lower()

    if query!="":
        speak("Opening"+query)
        os.system("start "+query)
    else:
        speak("not found")

def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+"on Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    patterns=r"play\s+(.*?)\s+on\s+youtube"
    match=re.serach(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None
