from network import WLAN
from mqtt
import machine import PIN
import time

def sub_cb(topic, msg):
   print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect("MJ", auth=(WLAN.WPA2, "10101010"), timeout=500)

while not wlan.isconnected():
    machine.idle()
print("Connected to Wifi\n")

client = MQTTClient("COM6", "io.adafruit.com",user="Manzi_12", password="d6412516e52e455489c3828acc110cd7", port=1883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="Manzi_12/feeds/speed")

while True:
    print("Sending ON")
    client.publish(topic="Manzi_12/feeds/speed", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="Manzi_12/feeds/speed", msg="OFF")
    client.check_msg()

    time.sleep(1)
