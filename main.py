import paho.mqtt.client as mqtt
import armario

mqttBroker ="test.mosquitto.org"
client = mqtt.Client("armarioC115Inatel")
client.connect(mqttBroker)

#Produto baseados em unidades
client.publish("Cozinha/Armario/Oleo", retain=True, qos=1, payload=6)
client.publish("Cozinha/Armario/CremeLeite", retain=True, qos=1, payload=3)
client.publish("Cozinha/Armario/Leite", retain=True, qos=1, payload=10)
client.publish("Cozinha/Armario/Condensado", retain=True, qos=1, payload=7)
client.publish("Cozinha/Armario/Molho", retain=True, qos=1, payload=5)
client.publish("Cozinha/Armario/Milho", retain=True, qos=1, payload=1)
client.publish("Cozinha/Armario/Ervilha", retain=True, qos=1, payload=4)

#Produtos baseados em Kg
client.publish("Cozinha/Armario/Arroz", retain=True, qos=1, payload=4.5)
client.publish("Cozinha/Armario/Feijao", retain=True, qos=1, payload=3.2)
client.publish("Cozinha/Armario/Cafe", retain=True, qos=1, payload=1.8)
client.publish("Cozinha/Armario/Sal", retain=True, qos=1, payload=1.1)
client.publish("Cozinha/Armario/Acucar", retain=True, qos=1, payload=2.8)
client.publish("Cozinha/Armario/Farinha", retain=True, qos=1, payload=1.5)