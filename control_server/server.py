from flask import Flask, request
from flask_socketio import SocketIO

bot_avail = False

try:
    import bot
    bot_avail = True
except:
    print('No bot control')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


socketio = SocketIO(app)


@socketio.on('move forward')
def move_forward():
    print('forward', 0.1)
    if bot_avail:
        bot.bot_forward()


@socketio.on('move backward')
def move_backward():
    print('backward', 0.1)
    if bot_avail:
        bot.bot_stop()


@socketio.on('turn left')
def turn_left():
    print('left', 0.1)
    if bot_avail:
        bot.bot_left()


@socketio.on('turn right')
def turn_right():
    print('right', 0.1)
    if bot_avail:
        bot.bot_right()


@socketio.on('rotate arm left')
def arm_rotate_left():
    print('arm rotate left', 0.1)
    if bot_avail:
        bot.plat_left()


@socketio.on('rotate arm right')
def arm_rotate_right():
    print('arm rotate right', 0.1)
    if bot_avail:
        bot.plat_right()

@app.route('/bbox', methods=['POST'])
def bbox():
    xmin = request.form.get('xmin')
    ymin = request.form.get('ymin')
    xmax = request.form.get('xmax')
    ymax = request.form.get('ymax')

    print(xmin, ymin, xmax, ymax)

    return "OK"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8100, debug=True)
