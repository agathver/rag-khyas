import cv2
from flask import Flask, render_template, Response
from model import detection_loop

app = Flask(__name__)


@app.route('/')
def index():
    return '<html><body><img src="/video_feed" /></body></html>'


def gen():
    for img in detection_loop():

        ret, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8190, debug=True)
