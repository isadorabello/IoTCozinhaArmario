from produto import Produto
import paho.mqtt.client as mqtt

mqttBroker ="test.mosquitto.org"
client = mqtt.Client("armarioC115Inatel")
client.connect(mqttBroker)
class Armario(object):

    def criandoProdutos(self, nome, min, max, atual, produtos):
        
        auxproduto = Produto(nome, min, max, atual)

        produtos.append(auxproduto)

        return produtos

    def to_json(self, produto):
        auxproduto = '{'
        
        for aux in produto:
            auxproduto += '"' + str(aux.nome) + '": "' + str(aux.atual) + '",'
        
        auxproduto += '}'

        return auxproduto

    def publish(self, produto):
        payload = self.to_json(produto=produto)
        client.publish("Cozinha/Armario", retain=True, qos=1, payload=payload)


