
import random
import datetime
import time

import json
import paho.mqtt.client as MQTT

# Create client instance
client = MQTT.Client()

# Setup login information
client.username_pw_set("tryusr", input('Password: '))

# Connect to MQTT listener
client.connect("127.0.0.1", 6677, 60)

while True:
    rand_num = random.randint(0, 30)
    t = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
    payload = {'Numbers of people': rand_num, 'Current Time': t}
    print(json.dumps(payload))

    #Publish to topic "test topic"
    client.publish("test_MQTT/test topic", json.dumps(payload))
    time.sleep(10)