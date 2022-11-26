import paho.mqtt.client as mqtt

class Conection:
    def __init__(self):
        mqttBroker ="test.mosquitto.org"
        self.client = mqtt.Client("armarioC115Inatel")
        self.client.connect(mqttBroker)