import paho.mqtt.client as mqtt
import time
from Block import BlockMqtt

client = mqtt.Client()
client.connect("localhost", 1883)

mydata = ""

def on_message(client, userdata, message):
  global mydata
  print(message.topic + " " + message.payload.decode('utf-8'))
  mydata = message.payload.decode('utf-8')

client.on_message = on_message
client.subscribe("test",qos=1)

client.loop_start()

while True:
    if len(mydata) != 0:
       break
       

client.loop_stop()
