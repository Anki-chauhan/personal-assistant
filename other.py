import datetime
from speaker import Speak


def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        print("good morning")
        Speak("good morning")
    elif (hour >= 12) and (hour <= 16):
        print("good afternoon")
        Speak("good afternoon")
    elif (hour >= 16) and (hour <= 20):
        print("good evening")
        Speak("good evening")
    else:
        print("nice to meet you")
        Speak("nice to meet you, in this time")


def goodbye():
    hour = datetime.datetime.now().hour
    if hour < 12:
        Speak("goodbye sir,have a good day")
        print("goodbye sir,have a good day")
    elif hour >= 12 or hour <= 13:
        Speak("bye sir,see you again")
        print("bye sir,see you again")
    else:
        Speak("goodnight sir,have a sweet dream")
        print("goodnight sir,have a sweet dream")
