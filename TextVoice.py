import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')  
engine.setProperty('rate', rate - 40)

recognizer = sr.Recognizer()

def voice():
    with sr.Microphone() as source:
        print('v_C')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Say something...")
        audio = recognizer.listen(source)
        print('v')
        text = recognizer.recognize_google(audio)
        print('rec:'+text)
        return text.lower()
def speech(text):   
    engine.say(text)
    engine.runAndWait()

