from calendar import month
import email
import queue
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
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard 
import os
import pyjokes
import string
import random

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

def sendEmail(receiver ,subject, content):                         # Send Email
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


def sendwhatsappmsg(phone_no, message):                          # Send Whatsapp message
    message = message
    wb.open('https://web.whatsapp.com/send?phone=' +phone_no+'&text='+message)
    #sleep(10)
    pyautogui.press('enter')


def screenshot():
    name_img = (datetime.datetime.now())
    name_img = 'C:\\Users\\camer\\Documents\\GitHub\\screenshot\\ss.png'
    img = pyautogui.screenshot(name_img)
    img.show()

    #https://api.openweathermap.org/data/2.5/weather?q=cape%20town,ZA&units=imperial&appid=b51e50c858815a087f5080752a24fc45

def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q=' +search)

def news():
    newsapi = NewsApiClient(api_key='a71bcc16634f4230b4ff06b67d2538cb')
    speak('what topic would you like to know about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q='topic',
                                    language = 'en', 
                                    page_size = 5) 
                                    
    newsdata = data['articles']                    
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("thats it for now ill update you sometime later.")


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed Cases: {data["cases"]} \n Deaths: {data["deaths"]} \n Recovered: {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)
    



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
                speak("Whatsapp message unsuccesful!")

        elif 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query. replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result) 
            speak(result)

        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak("what should I play on youtube?")
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            city = 'Cape Town'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=b51e50c858815a087f5080752a24fc45'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'][0] ['description']
            temp = round((temp -32) * 5/9) 
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is')
            speak('Temperature :{} degree celcius'.format(temp))
            speak('wearther is{}'.format(desp))


        elif 'news' in query:
            news()


        elif 'read' in query:
            text2speech()

        elif 'covid' in query:
            covid()

        elif 'open' in query:                              #open all from file explorer
            os.system('explorer C://{}'.format(query.replace('open','')))

        elif 'open code' in query:                         #open VScode
            codepath = 'C:\\Users\\camer\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()

        elif 'password' in query:
            passwordgen()

        elif 'offline' in query:
            quit()