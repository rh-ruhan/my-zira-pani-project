import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices [0].id)
# engine.setProperty('voice', voices[0].id)
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
   #  speak("hello ruhan. i am jarvis. how can i help you")
        speak("hello ruhan. i am zira. how can i help you")

#to send email
def sendEmail(to,contecnt):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('rhhimiru@gmail.com', '12345678')
    server.sendmail('rhhimiru@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:
        if 1:

         query = takecommand().lower()


        #logic building for tasks

         if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

         elif "open command prompt" in query:
            os.system("start cmd")


         elif "play music" in query:
            music_dir = "Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, song))


         elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address Sir {ip} ")



         elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            speak(result)
            # print(result)


         elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

         elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

         elif "open whatsapp" in query:
            webbrowser.open("www.whatsapp.com")

         elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

         elif "password" in query:
            pwd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567!@#$%^&*(')"
            res = ''.join(random.choices(pwd,k=7))
            speak(res)

         elif "send message" in query:  
            pywhatkit.sendwhatmsg("+8801304658602", "hello boss test msg",10,47)

         elif "play a song on youtube" in query:
            pywhatkit.playonyt("see you again")

         elif "email to rahat" in query:
            try:

               speak("what should i say?")
               content = takecommand().lower()
               to = "talhajubaer53774@gmail.com"
               sendEmail(to,content)
               speak("email has been sent to avi")

            except Exception as e:
              print(e)
              speak("sorry sir, i am not able to sent this email")




         elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

