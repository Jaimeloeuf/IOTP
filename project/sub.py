""" Dependencies """
# Client class to create MQTT Clients
from paho.mqtt.client import Client
import paho.mqtt.subscribe as subscribe

# Global variable to store the topic name, default topic is here too
topic = "JJ/is"
# Global variable to store the topic name, default topic is here too
broker = "m2m.eclipse.org"


def set_broker(data):
    # Function exposed to the other modules to set their own topics to publish to.
    global broker
    broker = data


def set_topic(data):
    # Function exposed to the other modules to set their own topics to publish to.
    global topic
    topic = data


def new_Msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))


def sub():
	subscribe.callback(new_Msg, topic, hostname=broker)
