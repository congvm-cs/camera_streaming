import imutils
from pyzbar import pyzbar
import cv2

class QRScanner(object):
    def __init__(self):
        pass

    def scan_return_image(self, frame):
        frame = imutils.resize(frame, width=400)

        # find the codes in the frame and decode each of the codes
        codes = pyzbar.decode(frame)

        # loop over the detected codes
        for code in codes:
            # extract the bounding box location of the code and draw
            # the bounding box surrounding the code on the image
            (x, y, w, h) = code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # the code data is a bytes object so if we want to draw it
            # on our output image we need to convert it to a string first
            codeData = code.data.decode("utf-8")
            codeType = code.type

            # draw the code data and code type on the image
            text = "{} ({})".format(codeData, codeType)
            cv2.putText(frame, text, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        return frame

    
    def scan_return_code(self, frame):
        frame = imutils.resize(frame, width=400)

        # find the codes in the frame and decode each of the codes
        codes = pyzbar.decode(frame)
        code = ""
        # loop over the detected codes
        # list_ret_code = []
        if len(codes) >= 1:
            code = codes[0].data.decode("utf-8")
            
        return len(codes), code