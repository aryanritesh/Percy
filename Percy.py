import sys
import pyttsx3
import pywhatkit
import speech_recognition as sr
import pyaudio
import os
import datetime
import cv2
from requests import get
import wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',170)
print(voices[2].id)
def speak(audio):
 engine.say(audio)
 print(audio)
 engine.runAndWait()

def takeRes(): #voice to text
  r=sr.Recognizer()
  with sr.Microphone() as source :
   print("detecting")
   r.pause_threshold=1
   audio=r.listen(source,timeout=2,phrase_time_limit=5)

   try:
     print("Recognizing..")
     question =r.recognize_google(audio,language='en-in')
     print(f"user said: {question}")

   except Exception as e:
     speak("I am sorry, Can you repeat?")
     return "none"
  return question

def greet():
    hour =int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning sir")
    elif hour>12 and hour<=17:
        speak("Good afternoon sir")
    elif hour>17 and hour<=20:
        speak("Good evening sir")
    elif hour>2 and hour<=4:
        speak("Sir you should consider sleeping")
    speak("Hey I am percy, how can I help you")

def sendEmail(to,content):
    emailAdd=os.environ.get('email_id')
    passAdd=os.environ.get('password_id')
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(emailAdd,passAdd)
    server.sendmail('emailAdd',to,content)
    server.close()


if __name__=="__main__":
 greet()
 while True:
    question=takeRes().lower()
    if "open notepad" in question:
       notePath="C:\\Windows\\system32\\notepad.exe"
       speak("opening notepad")
       os.startfile(notePath)
    elif "open word" in question:
        wordPath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
        speak("opening word")
        os.startfile(wordPath)
    elif "open command prompt" in question:
        speak("opening command prompt")
        os.system("start cmd")
    elif "open camera" in question:
        cap=cv2.VideoCapture(0)
        speak("opening camera")
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            k=cv2.waitKey(20)
            if k==10:
                break;
        cap.release()
        cv2.destroyAllWindows()
    elif "ip address" in question:
        speak("gathering information, hold on")
        ip= get('http://api.ipify.org').text
        speak(f"Your Ip address is {ip}")
    elif "search for" in question:
        speak("Looking it up..")
        question=question.replace("search for","")
        results = wikipedia.summary(question,sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif "youtube" in question:
#webbrowser.open("youtube.com")
     speak("Which video do you want me to play sir?")
     com=takeRes().lower()
     speak("loading...")
     pywhatkit.playonyt(f"{com}")
    elif "open google" in question:
    #webbrowser.Mozilla
     speak("What would you want me to search for sir?")
     com=takeRes().lower()
     #webbrowser.open(f"{com}")
     speak("Searching..")
     pywhatkit.search(f"{com}")
    elif "email" in question:
        speak("Who do you wish to send an email to sir?\n")
        email=input(speak)
        try:
            speak("What should be the subject sir?")
            subject=takeRes().lower()
            speak("What should be the content sir?")
            body=takeRes().lower()
            content=f'subject:{subject}\n\n{body}'
            to=email
            sendEmail(to,content)
            speak(f"The email has been sent to {email} sir")

        except Exception as e:
            print(e)
            speak("I am sorry sir, there was an error while sending the email")
    elif "no" in question:
        speak("Alright sir")
        sys.exit()

 speak("Is there anything else I can assist you with sir?")









