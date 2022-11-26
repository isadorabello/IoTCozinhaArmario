from model.produto import Produto
from conection.conection import Conection
import json

class Armario(Conection):

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

    def initSensor(self):
        msg = "init"
        self.clientSocket.send(msg.encode())
        return self.clientSocket.recv(1024).decode()

    def readSensor(self):
        return self.clientSocket.recv(1024).decode()


