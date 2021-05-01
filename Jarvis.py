import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning,Sir!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon,Sir!')
    else:
        speak('Good Evening,Sir!')
    speak('I am Jarvis. How may I help you')

def takeCommand():
    '''its takes microphone input from user and returns string output'''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        # print(e)
        print('Say that again please...')
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail.com','sender-pass')
    server.sendmail('senderemail.com',to,content)
    server.close()

if __name__=='__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=1)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            music_dir='D:\\English hits'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir,the time is {strTime}')
        elif 'open word' in query:
            wordPath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)
        elif 'open excel' in query:
            excelPath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excelPath)
        elif 'open powerpoint' in query:
            ppPath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppPath)
        elif 'email to jenish' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to = 'receiver@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to sent a email')
        elif 'your name' in query:
            speak('my name is jarvis and I was built by JBL on May first, 2021')

        elif 'bye bye' in query:
            speak('bye,Sir!')
            break

