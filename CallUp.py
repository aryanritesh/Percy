import speech_recognition as sr
import os
def takeRes():  # voice to text
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("detecting")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source)

            try:
                print("Recognizing..")
                question = r.recognize_google(audio, language='en-in')
                print(f"user said: {question}")

            except Exception as e:
                return takeRes()

            return question
while True:
    wakeUp=takeRes()
    if 'Percy' in wakeUp:
            os.startfile('C:\\Users\\aryan\\PycharmProjects\\P\\Percy.py')
    else:
            print("")