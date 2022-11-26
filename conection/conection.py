import paho.mqtt.client as mqtt

class Conection:
    def __init__(self):
        #Conectando ao mqtt
        mqttBroker ="test.mosquitto.org"
    
        self.client = mqtt.Client("armarioC115InatelCAP")
        self.client.connect(mqttBroker)