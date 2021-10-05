import sys
import ctypes
import time
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import requests
import os
import datetime
import cv2
from requests import get
import wikipedia
import smtplib
import geocoder
from geopy.geocoders import Nominatim
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from percyUi import Ui_Percy
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
import iconify as ico
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',170)
print(voices[2].id)
def speak(audio):
 engine.say(audio)
 print(audio)
 engine.runAndWait()

# def takeRes(): #voice to text
#   r=sr.Recognizer()
#   with sr.Microphone() as source :
#    print("detecting")
#    r.pause_threshold=1
#    audio=r.listen(source,timeout=2,phrase_time_limit=5)
#
#    try:
#      print("Recognizing..")
#      question =r.recognize_google(audio,language='en-in')
#      print(f"user said: {question}")
#
#    except Exception as e:
#       speak("I am sorry, Can you repeat?")
#       return takeRes()
#
#    return question

def greet():
    speak("Hey I am percy, how can I help you")
    hour =int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning sir")
    elif hour>12 and hour<=17:
        speak("Good afternoon sir")
    elif hour>17 and hour<=20:
        speak("Good evening sir")
    elif hour>2 and hour<=4:
        speak("Sir you should consider sleeping")


def sendEmail(to,content):
    emailAdd=os.environ.get('email_id')
    passAdd=os.environ.get('password_id')
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(emailAdd,passAdd)
    server.sendmail('emailAdd',to,content)
    server.close()

 #if __name__=="__main__":
class mainT(QThread):
   def __init__(self):
    super(mainT,self).__init__()
   def run(self):
       self.execute()
   def takeRes(self): #voice to text
      r=sr.Recognizer()
      with sr.Microphone() as source :
       print("detecting")
       r.pause_threshold=1
       audio=r.listen(source,timeout=2,phrase_time_limit=5)

       try:
         print("Recognizing..")
         self.question =r.recognize_google(audio,language='en-in')
         print(f"user said: {self.question}")

       except Exception as e:
          speak("I am sorry, Can you repeat?")
          return self.takeRes()

       return self.question
   def execute(self):
     greet()
     while True:
        self.question= self.takeRes().lower()
        if "open notepad" in self.question:
           notePath="C:\\Windows\\system32\\notepad.exe"
           speak("opening notepad")
           os.startfile(notePath)
        elif "open word" in self.question:
            wordPath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            speak("opening word")
            os.startfile(wordPath)
        elif "open command prompt" in self.question:
            speak("opening command prompt")
            os.system("start cmd")
        elif "open camera" in self.question:
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
        elif "ip address" in self.question:
            speak("gathering information, hold on")
            ip= get('http://api.ipify.org').text
            speak(f"Your Ip address is {ip}")
        elif "search for" in self.question:
            speak("Looking it up..")
            self.question=self.question.replace("search for","")
            results = wikipedia.summary(self.question,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "youtube" in self.question:
    #webbrowser.open("youtube.com")
         speak("Which video do you want me to play sir?")
         com= self.takeRes().lower()
         speak("loading...")
         pywhatkit.playonyt(f"{com}")
        elif "open google" in self.question:
        #webbrowser.Mozilla
         speak("What would you want me to search for sir?")
         com= self.takeRes().lower()
         #webbrowser.open(f"{com}")
         speak("Searching..")
         pywhatkit.search(f"{com}")
        elif "email" in self.question or "send an email" in self.question:
            speak("Who do you wish to send an email to sir?\n")
            email=input(speak)
            try:
                speak("What should be the subject sir?")
                subject= self.takeRes().lower()
                speak("What should be the content sir?")
                body= self.takeRes().lower()
                content=f'subject:{subject}\n\n{body}'
                to=email
                sendEmail(to,content)
                speak(f"The email has been sent to {email} sir")

            except Exception as e:
                print(e)
                speak("I am sorry sir, there was an error while sending the email")
        elif "close notepad" in self.question:
          speak("closing notepad..")
          os.system("TASKKILL/F /IM notepad.exe")
        elif "close browser" in self.question:
            speak("Are you sure sir?")
            resp= self.takeRes().lower()
            if "yes" in resp:
                os.system("TASKKILL/F /IM msedge.exe")
            elif "no" in resp:
                break;
        elif "dismiss word" in self.question or "close word" in self.question:
            speak("closing word")
            os.system("TASKKILL/F /IM WINWORD.exe")
        elif "joke" in self.question or "tell me a joke" in self.question:
         joke=pyjokes.get_joke(language='en',category='neutral')
         speak(joke)
        elif "turn off pc" in self.question or "shutdown the pc" in self.question:
            sd='shutdown /s /t1'
            os.system(sd)
        elif "restart pc" in self.question or "restart the pc" in self.question:
            r="shutdown /r /t 1"
            os.system(r)
        elif "lock screen" in self.question or "lock the screen" in self.question:
            ctypes.windll.user32.LockWorkStation()
        elif "tell me the news" in self.question:
            url='https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=de2d387b607b43bbb059f58b15020bae'
            speak("Here are the top 3 headlines for today")
            page=requests.get(url).json()
            articles=page["articles"]
            top3=["first","second","third"]
            header=[]
            for ar in articles:
                header.append(ar["title"])
            for i in range(len(top3)):
             speak(f"Today's {top3[i]} headline is :{header[i]}")
            speak("Do you want me to open the detailed news on the browser sir?")
            ans= self.takeRes().lower()
            if "yes" in ans:
                speak("opening google news..")
                pywhatkit.search("today's news")
            if "no" in ans:
                speak("Okay sir")
                break;
        elif "what is my location" in self.question or "where are we" in self.question:
          g= geocoder.ip('me')
          loc=g.latlng
          geoLoc = Nominatim(user_agent="GetLoc")
          name=geoLoc.reverse(loc)
          speak(name.address)
        elif "take a screenshot" in self.question or "screenshot" in self.question:
            speak("What should I name the file sir?")
            fileName= self.takeRes().lower()
            time.sleep(3)
            image=pyautogui.screenshot()
            image.save(f"{fileName}.png")
            speak("Done sir")

        elif "no thanks" in self.question or "shutdown" in self.question:
            speak("Alright sir")
            sys.exit()
        speak("Is there anything else I can assist you with sir?")

startProgram=mainT()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_Percy()
        self.ui.setupUi(self)
        button=self.ui.pushButton
        button.setStyleSheet("background - image: url(mic2.png);")
        self.ui.pushButton.clicked.connect(self.startTask)
    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:\\Users\\aryan\\Downloads\\percy3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startProgram.start()


app=QApplication(sys.argv)
Percy=Main()
Percy.show()
exit(app.exec_())





