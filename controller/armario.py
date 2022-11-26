from model.produto import Produto

class Armario(object):

    def createProduct(self, nome, min, max, atual, produtos):
        
        auxproduto = Produto(nome, min, max, atual)

        produtos.append(auxproduto)

        return produtos

    def to_json(self, produto):
        auxproduto = '{'
        for aux in produto:
            auxproduto += '"' + str(aux.nome) + '": "' + str(aux.atual) + '"'
            if(aux.nome != "Miojo"):
                auxproduto += ','
        
        auxproduto += '}'

        return auxproduto