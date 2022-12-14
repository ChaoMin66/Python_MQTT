import paho.mqtt.client as MQTT


# when successfully connected to mqtt server
def server_connected(client, userdata, flags, receive):
    print("Connected with result code "+str(receive))

    # Subscribe topics
    client.subscribe("test_MQTT/test topic")


# When message_received
def message_received(client, userdata, message):
    # decode message with utf-8
    print(f'{message.topic} {message.payload.decode("utf-8")}')


# Create client instance
subscriber = MQTT.Client()

# actions when connected
subscriber.on_connect = server_connected

# actions when receiving message
subscriber.on_message = message_received

# Setup login information
subscriber.username_pw_set("tryusr", input('Password: '))

# Connect to MQTT listener
subscriber.connect("127.0.0.1", 6677, 60)

# start connection with an infinite loop
subscriber.loop_forever()
