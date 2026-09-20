

import speech_recognition as sr
import pyttsx3

# Text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# Voice recognition
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except:
        speak("Sorry, I didn't understand.")
        return ""

speak("Hello sir. I am JARVIS. How can I help you?")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello sir. How are you?")

    elif "your name" in command:
        speak("My name is JARVIS.")

    elif "stop" in command or "exit" in command:
        speak("Goodbye sir.")
        break

    else:
        speak("I don't know that command yet.")