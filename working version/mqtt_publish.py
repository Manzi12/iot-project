# MQTT Publish Demo
# publish two message. to two differeent topics

import paho.mqtt.publish as publish

publish.single("speed/test", "fast",hostname="iot.eclipse.org")
print("done")
