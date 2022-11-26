from produto import Produto
from conection import Conection

class Armario(Conection):

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

    def publish(self, payload):
        result = self.client.publish(topic="Cozinha/Armario", retain=True, qos=1, payload=payload)
        print(result)


