import speech_recognition as sr
from speaker import Speak


def from_keyboard():
    data = input("type here")
    return data


def from_mic():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            Speak("mic is ready..")
            print("mic ready....say something")
            try:
                audio = r.listen(source)
                print("wait.....")
                data = r.recognize_google(audio)
                print("you said:", data)
                return data
            except:
                print("sorry! retry")
                Speak("sorry sir i can't recognize your voice")