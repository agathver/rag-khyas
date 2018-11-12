from flask import Flask
from flask_socketio import SocketIO
import bot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


socketio = SocketIO(app)


@socketio.on('move forward')
def move_forward():
    print('forward', 0.1)
    bot.bot_forward()


@socketio.on('move backward')
def move_backward():
    print('backward', 0.1)
    bot.bot_stop()


@socketio.on('turn left')
def turn_left():
    print('left', 0.1)
    bot.bot_left()


@socketio.on('turn right')
def turn_right():
    print('right', 0.1)
    bot.bot_right()


@socketio.on('rotate arm left')
def arm_rotate_left():
    print('arm rotate left', 0.1)
    bot.plat_left()


@socketio.on('rotate arm right')
def arm_rotate_right():
    print('arm rotate right', 0.1)
    bot.plat_right()


# if __name__ == '__main__':
#     socketio.run(app)
