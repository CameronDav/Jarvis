import pyttsx3 #pip install pyttsx3 == Text-Speech

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


while True:
    voice = int(input("Press 1 for male\nPress 2 for female\n"))
    # speak(audio)

    getvoices(voice)