import speech_recognition as sr
import pyautogui

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

    words = r.recognize_google(audio)
    print(f"You said: {words}")

pyautogui.moveTo(100, 100)

pyautogui.write(words)

