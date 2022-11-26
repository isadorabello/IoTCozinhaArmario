import paho.mqtt.client as mqtt
from socket import *

class Conection:
    def __init__(self):
        #Conectando ao mqtt
        mqttBroker ="test.mosquitto.org"
    
        self.client = mqtt.Client("armarioC115Inatel")
        self.client.connect(mqttBroker)
        
        #Criando um cliente local
        serverName = 'localhost'
        serverProt = 3000

        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((serverName, serverProt))