import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received on jetson subscriber")
    remote_client.publish("remoteface/image", message.payload)
    print("message published to cloud(ibm vsi) topic")

# remote mosquitto broker address on IBM virtual server
remote_broker_address="169.62.251.227"
#create new instance of client
remote_client = mqtt.Client("facepubremote")
#connect to broker
remote_client.connect(remote_broker_address,1883)

# mosquitto broker on jetson docker container
broker_address="172.18.0.2"
# creating new instance
client = mqtt.Client("facesub")
# attach function to callback
client.on_message=on_message
#connect to broker
client.connect(broker_address)

# subscribe to face/image topic
client.subscribe("face/image")
#wait to process callback
time.sleep(4)

client.loop_forever()
