from functions import *
from input import from_mic
from datetime import date

class Command:
    def __init__(self, data):
        if "music" in data:
            music()
        if "next song" in data:
            music()
        if "camera" in data:
            Camera()
        if "song list" in data:
            song_list()
        if "video list" in data:
            video_list()
        if "pause" in data:
            pause_music()
        if "resume" in data:
            resume_music()
        if "run" in data:
            search_video(data)
        if "videos" in data:
            video_player()
        if "screen recorder" in data:
            ScreenRecorder()
        if "search file" in data:
            search_directory()
        if "open" in data:
            open_website(data)
        if "tell me about" in data:
            tell_me_about(data)
        if "calculate age" in data:
            day = int(input("day"))
            month = int(input("month"))
            year = int(input("year"))
            dob = date(year, month, day)
            print("your date of birth is :", dob)
            cal_age(dob)

        if "play" in data:
            search_song(data)
        if "show image" in data:
            image_viewer()
        if "birthday" in data:
            date_of_birth()
        if "youtube" in data:
            youtube(data)
        if "make note" in data:
            Speak("What would you like me to write down?")
            print("what you want to note write here")
            note_text = from_mic()
            #note_text = input()
            note(note_text)
            Speak("I've made a note of that.")
            print("done")
        if "open chrome" in data:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        if "open microsoft office word" in data:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')
        if "shutdown" in data:
            os.system("shutdown /s /t 1")
        if "screenshot" in data:
            ss = pyautogui.screenshot()
            date1 = str(datetime.datetime.now())
            file = ss.save(date1.replace(':', '-')+'screenshot.jpg')




