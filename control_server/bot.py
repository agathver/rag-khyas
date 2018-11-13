import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from Queue import Queue
from threading import Thread

queue = Queue()

loop = True

def setup():
    GPIO.setup("P8_7", GPIO.OUT)
    GPIO.setup("P8_8", GPIO.OUT)
    GPIO.setup("P8_9", GPIO.OUT)
    GPIO.setup("P8_10", GPIO.OUT)
    GPIO.setup("P8_11", GPIO.OUT)
    GPIO.setup("P8_12", GPIO.OUT)
    GPIO.setup("P8_14", GPIO.OUT)
    GPIO.setup("P8_15", GPIO.OUT)
    GPIO.setup("P8_16", GPIO.OUT)
    GPIO.setup("P8_17", GPIO.OUT)
    GPIO.setup("P8_18", GPIO.OUT)
    GPIO.setup("P8_26", GPIO.OUT)
    GPIO.setup("P9_23", GPIO.OUT)
    GPIO.setup("P9_25", GPIO.IN)
    GPIO.setup("P9_27", GPIO.OUT)
    GPIO.setup("P9_15", GPIO.OUT)

    servo_pin = "P8_13"
    duty_min = 3
    duty_max = 14.5
    duty_span = duty_max - duty_min

    PWM.start(servo_pin, (100-duty_min), 60.0)
    duty = 100 - ((30 / 180) * duty_span + duty_min)

def start():
    global loop

    loop = True
    t = Thread(target=loop)
    t.daemon = True
    t.start()

def dispatch(action):
    global queue

    queue.put(action)

def loop():
    global loop

    while loop:
        action = queue.get()

        if action == 'bot_left':
            bot_left()
        elif action == 'bot_right':
            bot_right()
        elif action == 'bot_forward':
            bot_forward()
        elif action == 'bot_stop':
            bot_stop()
        elif action == 'plat_left':
            plat_left()
        elif action == 'plat_right':
            plat_right()
        elif action == 'servo_up':
            servo_up()
        elif action == 'servo_down':
            servo_down()


def bot_left():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.LOW)
    time.sleep(2)

def bot_right():
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)
    time.sleep(2)

def bot_forward():
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.LOW)
    time.sleep(2)

def bot_stop():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)
    time.sleep(2)

def plat_left():
    GPIO.output("P8_15", GPIO.HIGH)
    GPIO.output("P8_17", GPIO.LOW)
    time.sleep(2)

def plat_right():
    GPIO.output("P8_15", GPIO.LOW)
    GPIO.output("P8_17", GPIO.HIGH)
    time.sleep(2)

def servo_up():
    GPIO.output("P8_9", GPIO.HIGH)
    GPIO.output("P8_11", GPIO.LOW)
    PWM.set_duty_cycle(servo_pin, duty)
    PWM.stop(servo_pin)
    PWM.cleanup()

def servo_down():
    GPIO.output("P8_9", GPIO.LOW)
    GPIO.output("P8_11", GPIO.HIGH)
    PWM.set_duty_cycle(servo_pin, duty)
    PWM.stop(servo_pin)
    PWM.cleanup()

def stop():
    global loop
    loop = False

def get_distance():
    GPIO.setmode(GPIO.BCM)
    GPIO.output("P9_23", GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output("P9_23", GPIO.LOW)
    start = time.time()

    while GPIO.input("P9_25") == 0:
        start = time.time()

    while GPIO.input("P9_25") == 1:
        stop = time.time()

    elapsed = stop - start
    distance = (elapsed * 34300) / 2

    return distance

