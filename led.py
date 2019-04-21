from zeroconf import ServiceBrowser, Zeroconf, ServiceStateChange
from requests.auth import HTTPBasicAuth
import socket
import requests
import time

from zeroconf import ServiceBrowser, Zeroconf

"""imports for gpio led usage"""
import sys, time
import RPi.GPIO as GPIO


def fetch_ip():
    return (
        (
            [
                ip
                for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                if not ip.startswith("127.")
            ]
            or [
                [
                    (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                    for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                ][0][1]
            ]
        )
        + ["no IP found"]
    )[0]


ipNum = 0


#    def remove_service(self, zeroconf, type, name):
#       print("Service %s removed" % (name,))


class MyListener(object):
    # def remove_service(self, zeroconf, type, name):
    #   print("Service %s removed" % (name,))
    def __init__(self):
        self.name = 0

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        # print name, info.get_name(), info.server,
        if info.name == "team20_service._http._tcp.local.":
            self.name = socket.inet_ntoa(info.address)
        #    print(self.name)


if __name__ == "__main__":
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(1)

   # print(listener.name)
    url = "http://" + listener.name
    print(url)
    while 1:
        # print(globalAddress)
        #    url = "http://" + str(globalAddress)
        # print(url)
        #   r = requests.get(ipNum, auth=HTTPBasicAuth("admin", "secret"))
       # print("yes")
        break
"""Set led ports"""
redPin = 11
greenPin = 13
bluePin = 15

"""PWM functions"""
GPIO.setmode(GPIO.BOARD)
pwmRed = GPIO.PWM(11, 100)
pwmGreen = GPIO.PWM(13, 100)
pwmBlue = GPIO.PWM(15, 100)
dc = 100
# dcRed = 100
# dcGreen = 100
# dcBlue = 100

"""turn off warnings"""
GPIO.setwarnings(False)

"""LED Functions"""


def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


"""PWM lightups"""


def bright(pwm, newdc):
    pwm.start(100)
    pwm.ChangeDutyCycle(newdc)


def dark(pwm):
    pwm.ChangeDutyCycle(0)
    pwm.stop()


"""LED and PWM lightups"""


def redOn():
    blink(redPin)
    bright(pwmRed, dc)


def greenOn():
    blink(greenPin)
    bright(pwmGreen, dc)


def blueOn():
    blink(bluePin)
    bright(pwmBlue, dc)


def yellowOn():
    blink(redPin)
    bright(pwmRed, dc)
    blink(greenPin)
    bright(pwmGreen, dc)


def cyanOn():
    blink(greenPin)
    bright(pwmGreen, dc)
    blink(bluePin)
    bright(pwmBlue, dc)


def magentaOn():
    blink(redPin)
    bright(pwmRed, dc)
    blink(bluePin)
    bright(pwmBlue, dc)


def whiteOn():
    blink(redPin)
    bright(pwmRed, dc)
    blink(greenPin)
    bright(pwmGreen, dc)
    blink(bluePin)
    bright(pwmBlue, dc)


def redOff():
    turnOff(redPin)
    dark(pwmRed)


def greenOff():
    turnOff(greenPin)
    dark(pwmGreen)


def blueOff():
    turnOff(bluePin)
    dark(pwmBlue)


def yellowOff():
    turnOff(redPin)
    dark(pwmRed)
    turnOff(greenPin)
    dark(pwmGreen)


def cyanOff():
    turnOff(greenPin)
    dark(pwmGreen)
    turnOff(bluePin)
    dark(pwmBlue)


def magentaOff():
    turnOff(redPin)
    dark(pwmRed)
    turnOff(bluePin)
    dark(pwmBlue)


def whiteOff():
    turnOff(redPin)
    dark(pwmRed)
    turnOff(greenPin)
    dark(pwmGreen)
    turnOff(bluePin)
    dark(pwmBlue)
