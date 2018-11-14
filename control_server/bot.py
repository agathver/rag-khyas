import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

def stop_all_motors():
    # forward / back
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)

    # servo
    GPIO.output("P8_15", GPIO.LOW)
    GPIO.output("P8_17", GPIO.LOW)

    # suction
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)

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
    GPIO.setup("P9_25", GPIO.OUT)
    GPIO.setup("P9_27", GPIO.OUT)
    GPIO.setup("P9_15", GPIO.OUT)

    servo_pin = "P8_13"
    duty_min = 3
    duty_max = 14.5
    duty_span = duty_max - duty_min

    PWM.start(servo_pin, (100-duty_min), 60.0)
    duty = 100 - ((30 / 180) * duty_span + duty_min)

    stop_all_motors()


def bot_left():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.LOW)
    #time.sleep(2)

def bot_right():
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)
    #time.sleep(2)

def bot_forward():
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.LOW)
    time.sleep(2)
    bot_stop()

def bot_stop():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)
    #time.sleep(0.2)

def plat_left():
    GPIO.output("P8_15", GPIO.HIGH)
    GPIO.output("P8_17", GPIO.LOW)
    #time.sleep(0.2)
    #plat_right()

def plat_right():
    GPIO.output("P8_15", GPIO.LOW)
    GPIO.output("P8_17", GPIO.HIGH)
    #time.sleep(0.2)

def suction_start():
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.HIGH)

def suction_end():
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)

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

