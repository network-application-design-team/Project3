from zeroconf import ServiceBrowser, Zeroconf, ServiceStateChange
from requests.auth import HTTPBasicAuth
import socket
import requests
import time
import json
from zeroconf import ServiceBrowser, Zeroconf
from html.parser import HTMLParser 
import pdb
"""imports for gpio led usage"""
import sys, time
import RPi.GPIO as GPIO
from bs4 import BeautifulSoup
GPIO.setwarnings(False)
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

status = ''
color = ''
brightness = ''

redPin = 11
greenPin = 13
bluePin = 15


GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

pwmRed = GPIO.PWM(redPin, 100)
pwmRed.start(0)
pwmGreen = GPIO.PWM(greenPin, 100)
pwmGreen.start(0)
pwmBlue = GPIO.PWM(bluePin, 100)
pwmBlue.start(0)



def blink(pin, pwm, newdc):
    pwm.ChangeDutyCycle(newdc)

#def turnOff(pin, pwm, newdc):
#    GPIO.setmode(GPIO.BOARD)
#    GPIO.setup(pin, GPIO.OUT)
#    GPIO.output(pin, GPIO.LOW)

"""LED and PWM lightups"""

def red(dc):
    blink(redPin, pwmRed, dc)


def green(dc):
    blink(greenPin, pwmGreen, dc)


def blue(dc):
    blink(bluePin, pwmBlue, dc)


def yellow(dc):
    blink(redPin, pwmRed, dc)
    blink(greenPin, pwmGreen, dc)


def cyan(dc):
    blink(greenPin, pwmGreen, dc)
    blink(bluePin, pwmBlue, dc)


def magenta(dc):
    blink(redPin, pwmRed, dc)
    blink(bluePin, pwmBlue, dc)


def white(dc):
    blink(redPin, pwmRed, dc)
    blink(greenPin, pwmGreen, dc)
    blink(bluePin, pwmBlue, dc)

















if __name__ == "__main__":
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(1)
    parser = HTMLParser()
   # print(listener.name)
    url = "http://" + listener.name
    oldColor = "white"
    oldLed = "off"
    oldDim = 0
    color = "white"
    status = "off"
    intensity = 0
#    print(url)
    while 1:
        # print(globalAddress)
        #    url = "http://" + str(globalAddress)
        # print(url)
        time.sleep(10)
        r = requests.get(url, auth=HTTPBasicAuth("Buse", "Honaker"))
            
        data = r.text
#        print(data)
 
        soup = BeautifulSoup(r.text, 'html.parser')
        listSoup = soup.find_all("h2")
        colorTag = str(listSoup[1])
        ledTag = str(listSoup[2])
        dimTag = str(listSoup[3])
        c = "<h2>Color : "
        l = " </h2>"
        x = "<h2>LED : "
        y = "<h2>Dimness : "
        color = colorTag[len(c):-len(l)]
        status = ledTag[len(x):-len(l)]
        intensity = int(dimTag[len(y):-len(l)])
        if status == 'on':
            if color == 'red':
                dc = 0
                blue(dc)
                green(dc)
                dc = intensity
                red(dc)
            elif color == 'green':
                dc = 0
                red(dc)
                blue(dc)
                dc = intensity
                green(dc)
            elif color == 'blue':
                dc = 0
                red(dc)
                green(dc)
                dc = intensity
                blue(dc)
            elif color == 'yellow':
                dc = 0
                blue(dc)
                dc = intensity
                yellow(dc)
            elif color == 'cyan':
                dc = 0
                red(dc)
                dc = intensity
                cyan(dc)
            elif color == 'magenta':
                dc = 0
                green(dc)
                dc = intensity
                magenta(dc)
            elif color == 'white':
                dc = intensity
                white(dc)
            else:
                print('ERROR: Unknown Color Request')
        elif status == 'off':
            if color == 'red':
                dc = 0
                red(dc)
            elif color == 'green':
                dc = 0
                green(dc)
            elif color == 'blue':
                dc = 0
                blue(dc)
            elif color == 'yellow':
                dc = 0
                yellow(dc)
            elif color == 'cyan':
                dc = 0
                cyan(dc)
            elif color == 'magenta':
                dc = 0
                magenta(dc)
            elif color == 'white':
                dc = 0
                white(dc)
            else:
                print('ERROR: Unknown Color Request')
        else:
            print('ERROR: Unknown Status Request')









      #  print(soup.prettify())
#        pdb.set_trace()
       # parsedData = parser.feed(data)
       # print(parser.)
       # print(r.text)
        #status = r.text
        # print("yes")
        #print(status)
        
"""Set led ports"""
redPin = 11
greenPin = 13
bluePin = 15

"""PWM functions"""

dc = 100
pwm = ''



"""turn off warnings"""
GPIO.setwarnings(False)

"""LED Functions"""


def blink(pin, pwm, newdc):
    pwm.ChangeDutyCycle(newdc)

"""LED and PWM lightups"""

def red(dc):
    blink(redPin, pwmRed, dc)


def green(dc):
    blink(greenPin, pwmGreen, dc)


def blue(dc):
    blink(bluePin, pwmBlue, dc)


def yellow(dc):
    blink(redPin, pwmRed, dc)
    blink(greenPin, pwmGreen, dc)


def cyan(dc):
    blink(greenPin, pwmGreen, dc)
    blink(bluePin, pwmBlue, dc)


def magenta(dc):
    blink(redPin, pwmRed, dc)
    blink(bluePin, pwmBlue, dc)


def white(dc):
    blink(redPin, pwmRed, dc)
    blink(greenPin, pwmGreen, dc)
    blink(bluePin, pwmBlue, dc)
