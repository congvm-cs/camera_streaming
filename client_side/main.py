#!/usr/bin/env python
from flask import Flask, render_template, Response, jsonify
from camera import VideoCamera
import base64

app = Flask(__name__)

cap = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/get_frame', methods=['GET'])
# def frame_extract():
#     frame = gen(cap)
#     print(base64.b64encode(frame))

#     _response = {
#         "data": base64.b64encode(frame)
#     }
#     return jsonify(_response)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)