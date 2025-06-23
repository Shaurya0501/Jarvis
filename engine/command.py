import pyttsx3
import speech_recognition as sr
import eel
import time

eel.init('web')  # folder containing HTML

def speak(text):
    try:
        engine = pyttsx3.init()  # default engine, cross-platform
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # female voice
        engine.setProperty('rate', 174)
        eel.displayMessage(text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print(f"Mic error: {e}")
            return ""

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}')
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        print("Recognition error:", e)
        return ""

    eel.ShowHood()
    return query.lower()

@eel.expose
def allCommands():

    query=takecommand()
    print(query)

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)

    elif "on youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print("not run")

    eel.showHood()