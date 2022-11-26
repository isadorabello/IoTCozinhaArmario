import time
from armario import Armario
from listacompra import ListaCompra

#instanciando um armario
armario = Armario()

#instanciando um lista de compras
listacompra = ListaCompra()

#Criando um vetor de produtos vazios
produtos = []

#Produtos pre-definidos
criarprodutos = [
    ["Arroz", 0, 5, 4.1],
    ["Feijao", 0, 5, 0],
    ["Cafe", 0, 2, 0],
    ["Sal", 0, 2, 0.1],
    ["Acucar", 0, 5, 2.4],
    ["Farinha", 0, 2, 1.7],
    ["Oleo", 0, 10, 1],
    ["Leite", 0, 10, 2],
    ["Molho", 0, 10, 3],
    ["CremeLeite", 0, 10, 4],
    ["Condensado", 0, 10, 5],
    ["Milho", 0, 10, 7],
    ["Ervilha", 0, 10, 2],
    ["Miojo", 0, 10, 8],
]

#Inserindo os produtos pre-definido no vetor de produtos
for aux in criarprodutos:
    produtos = armario.criandoProdutos(aux[0], aux[1], aux[2], aux[3], produtos)


armario.publish(armario.to_json(produto=produtos))
time.sleep(1)
listacompra.Calculate(produtos=produtos)