import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
def speak(audio):
 engine.say(audio)
 print(audio)
 engine.runAndWait()

def takeRes(): #voice to text
  r=sr.Recognizer()
  with sr.Microphone() as source :
   print("detecting")
   r.pause_threshold=1
   audio=r.listen(source,timeout=1,phrase_time_limit=5)

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
    elif hour>17 and hour<=8:
        speak("Good evening sir")
    elif hour>2 and hour<=4:
        speak("Sir you should consider sleeping")
    speak("I am percy, how can I help you")



if __name__=="__main__":
 greet()
 if 1:
    question=takeRes().lower()
    if "open notepad" in question:
       notePath="C:\\Windows\\system32\\notepad.exe"
       os.startfile(notePath)
    elif "open word" in question:
        wordPath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
        os.startfile(wordPath)


