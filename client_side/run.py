import numpy as np
import cv2
from qrscanner import QRScanner
import requests
import json
import time
import threading
from threading import Thread
import pygame
# from playsound import playsound

URL = 'http://10.2.72.39:15000/api/charge'



def say_welcome():    
    pygame.mixer.init()
    pygame.mixer.music.load("./audios/welcome.wav")
    pygame.mixer.music.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)
    # while pygame.mixer.music.get_busy() == True:
    #     continue


def say_yes():    
    pygame.mixer.init()
    pygame.mixer.music.load("./audios/comein.wav")
    pygame.mixer.music.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)
    # while pygame.mixer.music.get_busy() == True:
    #     continue

def say_no():    
    pygame.mixer.init()
    pygame.mixer.music.load("./audios/invalid.wav")
    pygame.mixer.music.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)
    # while pygame.mixer.music.get_busy() == True:
    #     continue


def request(code):
    payload = {'code': code}
    headers = {'content-type': 'application/json'}
    byte_res = requests.post(URL, data=json.dumps(payload), headers=headers)
    # print(response.content)

    str_res = byte_res.content.decode("utf-8")
    dict_res = eval(str_res)

    status = dict_res['status']
    print('status: {}'.format(status))

    if status == 'false':
        say_no()
    
    if status == 'true':
        say_yes()
    

qrscanner = QRScanner()
cap = cv2.VideoCapture(-1)

str_code = ""
str_temp_code = ""

TIMEOUT = 3

prev_t = time.time()

# Welcome
t = Thread(target=say_welcome, args=())
t.start()

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        n_codes, str_code = qrscanner.scan_return_code(frame)
        # print("str_code: {}".format(str_code))
        # print("str_temp_code: {}".format(str_temp_code))

        if (n_codes >= 1) & (str_code != str_temp_code):
            print("Capture")

            t = Thread(target=request, args=(str_code,))
            t.start()
            
            str_temp_code = str_code

        
        if time.time() - prev_t >= TIMEOUT:
            str_temp_code = ""
            prev_t = time.time()

        # break
        # qrscanner.scan_return_code(frame)
        # cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
