from calendar import month
import email
from unicodedata import name
import pyttsx3 #pip install pyttsx3 == Text-Speech
import datetime
import speech_recognition as sr # pip install SpeechRecognition.
import smtplib 
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep

engine = pyttsx3.init()

def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello with is jarvis")

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello with is Martha")

    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #I=Hours M=minutes S=seconds
    speak("The Current Time Is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir")
    elif hour >= 12 and hour <12:
        speak("good afternoon sir")
    elif hour >=18 and hour <24:
        speak("Good evening sir")
    else:
        speak("good Night sir")

def wishme():
   # speak("Welcome back sir!")
   # time()
   # date()
   # greeting()
    speak("I am at your service, please tell me how i can help you?")


#while True:F
   # voice = int(input("Press 1 for male\nPress 2 for female\n"))
    # speak(audio)

    #getvoices(voice)

#time()
#date()
#wishme()

def takeCommandCmd():
    query = input("please tell can how i can help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio , language='en-ZA')
        print(query)
    except Exception as e:
        print(e)
        speak("please say that again!")
        return "None"
    return query 

def sendEmail(receiver ,subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['from'] = senderemail
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def sendwhatsappmsg(phone_no, message):
    message = message
    wb.open('https://web.whatsapp.com/send?phone=' +phone_no+'&text='+message)
    sleep(10)
    pyautogui.press('enter')


if __name__ == "__main__":
    getvoices(2)
    wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'email' in query:
            email_list = {  #Email Addresses go hear..... In future try and create a csv file containing all emails address.
                'Cameron' : 'cameron.davids@younglings.africa', 'Russell' : 'russel.magaya@younglings.africa'

            }
            try:
                speak("To who should i send a email to?")
                name = takeCommandMic()
                reciever = email_list[name]
                speak("what is the subject of this email?")
                subject = takeCommandMic()
                speak('what should i say')
                content = takeCommandMic()
                sendEmail(reciever, subject, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak("unable to send email.")


        elif'message' in query:
            user_name = {
                'Cameron': '+27 61 441 9347',
                'mo': '+27 84 682 2539',
                'Josh': '+27 65 873 8753',
                'Russell' : '+27 68 161 7207',
                'Tristan' : '+27 67 963 9611'

            }
            try:
                speak("To who should i send a whatsapp Message?")
                name = takeCommandMic()
                phone_number = user_name[name]
                speak("what is the Message?")
                message = takeCommandMic()
                sendwhatsappmsg(phone_number,message)
                speak('Whatsapp message has been sent')
            except Exception as e:
                print(e)
                speak("Whatsapp message unseuccesful!")



        elif 'offline' in query:
            quit()



