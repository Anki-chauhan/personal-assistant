from input import from_keyboard, from_mic
from commands import Command
from other import *
#from textpreprocessing import TextProcessing
wish()
while True:
    user_text = from_keyboard()
    #user_text = TextProcessing(user_text)
    obj1 = Command(user_text)
    if user_text == "mic":
        while True:
            user_text = from_mic()
            Command(user_text)
            if "goodbye" == user_text or "bye" == user_text or "terminate" == user_text:
                goodbye()
                break
            if "keyboard" == user_text:
                break
    if "goodbye" == user_text or "bye" == user_text or "terminate" == user_text:
        goodbye()
        break
    else:
        continue


