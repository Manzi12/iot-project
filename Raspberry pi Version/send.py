# Import library and create instance of REST client.
from Adafruit_IO import Client
from time import sleep
aio = Client('ADAFRUIT KEY')

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
my_pwm=GPIO.PWM (13, 1000)

# Add the value 98.6 to the feed 'Temperature'.
my_pwm.start(60)
while True:
    for i in range(70,100):
        my_pwm.ChangeDutyCycle(i)
        sleep(1)
        speed = i
        print('speed: {0}'.format(speed))
        aio.send('speed', i)

