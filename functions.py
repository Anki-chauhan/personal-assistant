from PIL import Image
#from datetime import *
import datetime
import numpy as np
import pyautogui
import urllib
import re
import os
import random
from pygame import mixer
import cv2
from time import sleep
from speaker import Speak
import wikipedia
import webbrowser


def youtube(data):
    reg_ex = re.search('youtube (.+)', data)
    if reg_ex:
        domain = reg_ex.group(1)
        query_string = urllib.parse.urlencode({"search_query": domain})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        url = 'https://www.youtube.com/watch?v={}'.format(search_results[0])
        webbrowser.open(url)


def date_of_birth():
    dob = date(1996, 7, 8)
    dob = (dob.strftime("%d"), dob.strftime("%B"), dob.year)
    Speak(dob)
    print(dob)


def image_viewer():
    Speak("whom image you wanna to see")
    data = input("who's image")
    if "amit" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\kargil")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\kargil\\" + str(image)).show()
    elif "sachin" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\sachin")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\sachin\\" + str(image)).show()
    elif "kargil life" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\jahnavi")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\jahnavi\\" + str(image)).show()
    elif "sanobar" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\sanobar")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\sanobar\\" + str(image)).show()
    elif "jahnavi" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\jahnavi")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\jahnavi\\" + str(image)).show()
    elif "supriya" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\supriya")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\supriya\\" + str(image)).show()
    elif "urusha" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\urusha")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\urusha\\" + str(image)).show()
    elif "ankit" in data:
        image_list = os.listdir(r"E:\image_recognizer\Images\ankit")
        for image in image_list:
            img = Image.open(r"E:\image_recognizer\Images\ankit\\" + str(image)).show()
    else:
        Speak("sorry sir here is not present what you want to see")
        Speak("see another photos")
        image_list = os.listdir(r"F:\PICTURES\images\New folder")
        for image in image_list:
            if image.endswith(".jpg"):
                img = Image.open(r"F:\PICTURES\images\New folder\\" + str(image))
                img.show()


def cal_age(bod):
    today = date.today()
    year = today.year - bod.year
    if today.month < bod.month:
        month = (12 - bod.month + today.month)
    else:
        month = (today.month - bod.month)
    if today.day < bod.day:
        day = (30 - today.day + bod.day)
    else:
        day = (today.day - bod.day)
    age = (str(year) + "year", str(month) + "month", str(day) + "day")
    print("your age is:", age)
    Speak(age)



def tell_me_about(data):
    reg_ex = re.search('tell me about (.*)', data)
    if reg_ex:
        topic = reg_ex.group(1)
        ny = wikipedia.page(topic)
        p = ny.content[:500].encode('utf-8')
        print(p)
        Speak(p)


def open_website(data):
    reg_ex = re.search('open (.+)', data)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)


def search_directory():
    Speak("tell file name or extention of file")
    print("type file name or extention of file")
    search_file = input("search for any file:")
    for r, d, f in os.walk("G:"):
        for files in f:
            if files.startswith(search_file) or files.endswith(search_file):
                print(files)


def song_list():
    for r, d, f in os.walk("G:/all songs/audio"):
        for file in f:
            print(file)


def search_song(data):
    reg_ex = re.search('play (.+)', data)
    if reg_ex:
        domain = reg_ex.group(1)
        for r, d, f in os.walk("G:/all songs/audio"):
            for files in f:
                if files.startswith(domain):
                    print(files)
                    os.chdir("G:/all songs/audio")
                    files = os.path.abspath(files)
                    mixer.init()
                    mixer.music.load(files)
                    mixer.music.play()


def search_video(data):
    reg_ex = re.search('run (.+)', data)
    if reg_ex:
        domain = reg_ex.group(1)
        file_dir = os.listdir("G:/video/New folder")
        for files in file_dir:
            if files.startswith(domain):
                print(files)
                os.chdir("G:/video/New folder")
                files = os.path.abspath(files)
                os.system(files)


def video_player():
    list_video = []
    file_type = [".mp4", ".avi", ".mkv"]
    file_dir = os.listdir("G:/video/New folder")
    for file in file_dir:
        for i in file_type:
            if file.endswith(i):
                list_video.append(file)
    p = random.choice(list_video)
    print(p)
    os.chdir("G:/video/New folder")
    r = os.path.abspath(p)
    print(r)
    os.system(r)


def pause_music():
    mixer.music.pause()


def resume_music():
    global pause
    mixer.music.unpause()
    pause = False


def video_list():
    file_dir = os.listdir("G:/video/New folder")
    for file in file_dir:
        print(file)


def music():
    list_audio = []
    for root, directory, file in os.walk("G:/all songs/mp3"):
        for d in file:
            if d.endswith(".mp3"):
                list_audio.append(d)
    o = random.choice(list_audio)
    print(o)
    os.chdir("G:/all songs/mp3")
    j = os.path.abspath(o)
    print(j)
    mixer.init()
    mixer.music.load(j)
    mixer.music.play()


def note(text):
    date1 = datetime.datetime.now()
    file_name = str(date1).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        return


class Camera:
    def __init__(self):
        cam = cv2.VideoCapture(0)
        sleep(2)
        i = 0
        while True:
            try:
                check, frame = cam.read()
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    i = i+1
                    file = "image"+str(i)+".jpg"
                    cv2.imwrite(filename=file, img=frame)
                    print("Image saved!:", file)
                    continue

                elif key == ord('q'):
                    cam.release()
                    cv2.destroyAllWindows()
                    break

            except KeyboardInterrupt:
                print("Turning off camera.")
                cam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break


class ScreenRecorder:
    def __init__(self):
        screen_size = (1366, 768)
        vr = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("recording.avi", vr, 20.0, screen_size)
        print("Start Recording")
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            out.write(frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                print("stop recording")
                break
        out.release()
        cv2.destroyAllWindows()