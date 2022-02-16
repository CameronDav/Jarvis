import pyttsx3 #pip install pyttsx3 == Text-Speech
import datetime

engine = pyttsx3.init()

def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)


    if voice == 2:
        engine.setProperty('voice', voices[1].id)

    speak("hello with is jarvis")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #I=Hours M=minutes S=seconds
    speak("The Current Time Is:")
    speak(Time)


#while True:
   # voice = int(input("Press 1 for male\nPress 2 for female\n"))
    # speak(audio)

    #getvoices(voice)

time()