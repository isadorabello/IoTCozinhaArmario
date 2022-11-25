import paho.mqtt.client as mqtt
import armario
import time

mqttBroker ="test.mosquitto.org"
client = mqtt.Client("armarioC115Inatel")
client.connect(mqttBroker)

ListaCompra = [" "]*13
ListaCompra[0] = "Arroz"

for i in ListaCompra:
    client.publish("Cozinha/ListaCompras", retain=True, qos=1, payload=i)
    time.sleep(1)