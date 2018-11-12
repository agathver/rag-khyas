from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


socketio = SocketIO(app)


@socketio.on('move forward')
def move_forward():
    print('forward', 0.1)


@socketio.on('move backward')
def move_backward():
    print('backward', 0.1)


@socketio.on('turn left')
def turn_left():
    print('left', 0.1)


@socketio.on('turn right')
def turn_right():
    print('right', 0.1)


@socketio.on('rotate arm left')
def arm_rotate_left():
    print('arm rotate left', 0.1)


@socketio.on('rotate arm right')
def arm_rotate_right():
    print('arm rotate right', 0.1)


# if __name__ == '__main__':
#     socketio.run(app)
