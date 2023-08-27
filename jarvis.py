import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import webbrowser
import random2
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("hello I am your virtual assistant , how can I help u ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising....")
        speak("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: (query)\n")

    except Exception:
        print("say it again please.......")
        return"none"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching.......")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            break
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            break
        elif'open gmail' in query:
            webbrowser.open("gmail.com")
            break

        elif 'play music' in query:
            music_dir = 'D:\\music\\mashup'
            n = random2.randint(0, 190)
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[n]))
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H%M")
            speak(f"sir , the time is " + strTime)
            break
