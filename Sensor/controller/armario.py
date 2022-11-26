from model.produto import Produto
import json

class Armario(object):

    def createProduct(self, nome, min, max, atual, produtos):
        
        auxproduto = Produto(nome, min, max, atual)

        produtos.append(auxproduto)

        return produtos

    def to_json(self, produto):
        auxproduto = '{'
        
        for aux in produto:
            auxproduto += '"' + str(aux.nome) + '": "' + str(aux.atual) + '",'
        
        auxproduto += '}'

        return auxproduto

    def publish(self, payloadjson):
        result = self.client.publish(topic="Cozinha/Armario", retain=True, qos=1, payload=payloadjson)
        print(result)

    # def initSensor(self):
    #     msg = "init"
    #     self.clientSocket.send(msg.encode())
    #     return json.loads(self.clientSocket.recv(1024).decode())

    # def readSensor(self):
        # return json.loads(self.clientSocket.recv(1024).decode())


