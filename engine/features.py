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
    app_name = query.strip()

    if app_name != "":


        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

       


def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+"on Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    patterns=r"play\s+(.*?)\s+on\s+youtube"
    match=re.serach(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None
