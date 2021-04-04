import pyttsx3


class Speak:
    def __init__(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 200)
        engine.setProperty('volume', 1)
        engine.setProperty('voice', 5)
        engine.say(text)
        engine.runAndWait()