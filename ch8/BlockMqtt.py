import datetime
import hashlib
import paho.mqtt.client as mqtt

# global
mydata = ""

def on_message(client, userdata, message):
  global mydata
  print(message.topic + " " + message.payload.decode('utf-8'))
  mydata = message.payload.decode('utf-8')

client = mqtt.Client()
client.connect("localhost", 1883)

client.on_message = on_message
client.subscribe("test",qos=1)


class BlockMqtt:
    hashFunction = ""
    bHash = ""
    def __init__(self,prevHash, data):
        global mydata
        mydata = ""
        self.prevHash = prevHash
        self.data = data
        self.time = datetime.datetime.now()
        self.nonce = 0
        self.bHash = self.compHash()
        self.interrupted = False

    def compHash(self):
        hashFunction = hashlib.new('sha256')
        myStr = str(self.prevHash)+str(self.data)+str(self.time)+str(self.nonce)
        myBytes = myStr.encode()
        hashFunction.update(myBytes)
        self.bHash = hashFunction.hexdigest()
        return self.bHash

    def mine(self,diff):
        global mydata
        mydata = ""
        self.interrupted = False

        client.loop_start()
        self.target = "0"*diff
        while self.bHash[0:diff] != self.target:
            if len(mydata) != 0:
               print("break")
               self.interrupted = True
               break
            self.nonce = self.nonce + 1
            self.compHash()
        #print("Block mined: ", self.bHash)
        return self

    def update(self,prevHash,data):
        self.prevHash = prevHash
        self.data = data

    def __str__(self):
        s = 'prevHash: '+ self.prevHash + '\n'
        s = s + 'data: ' + self.data + '\n'
        s = s + 'time: ' + str(self.time) + '\n'
        s = s + 'nonce: ' + str(self.nonce) + '\n'
        s = s + 'interrupted: ' + str(self.interrupted) + '\n'
        s = s + 'bHash: ' + self.bHash + '\n'

        return s
