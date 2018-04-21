# Import library and create instance of REST client.
from Adafruit_IO import Client
from time import sleep
aio = Client('316faa4ea3654e338602246bed347b2c')

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
my_pwm=GPIO.PWM (13, 1000)

# Get the last value of the temperature feed.


# Print the value and a message if it's over 100.  Notice that the value is
# converted from string to int because it always comes back as a string from IO.


#print('speed: {0}'.format(speed))
    
my_pwm.start(60)
while True:
        data = aio.receive('speed')
        speed = int(data.value)
        my_pwm.ChangeDutyCycle(speed)
        speed = data
        print('speed: {0}'.format(speed))