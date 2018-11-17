import numpy as np
import cv2
from qrscanner import QRScanner
import requests
import json
import time
import threading


from threading import Thread


def request(code):
    payload = {'code': code}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.content)

    


url = 'http://10.2.72.39:15000/api/charge'

qrscanner = QRScanner()
cap = cv2.VideoCapture(1)


img = cv2.imread('./images/Qr-3.png')
code = qrscanner.scan_return_code(img)

str_code = ""
str_temp_code = ""

TIMEOUT = 3

prev_t = time.time()

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # Scan QRCode
        n_codes, str_code = qrscanner.scan_return_code(frame)
        # print("str_code: {}".format(str_code))
        # print("str_temp_code: {}".format(str_temp_code))

        if (n_codes >= 1) & (str_code != str_temp_code):
            t = Thread(target=request, args=(str_code,))
            t.start()
            str_temp_code = str_code

        
        if time.time() - prev_t >= TIMEOUT:
            str_temp_code = ""
            prev_t = time.time()

        # break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
