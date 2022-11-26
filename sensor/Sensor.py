
from controller.armario import Armario

#Criando um vetor de produtos vazio
produtos = []

#Produtos pre-definidos
criarprodutos = [
    ["Arroz", 0, 5, 2.1],
    ["Feijao", 0, 5, 2],
    ["Cafe", 0, 2, 0],
    ["Sal", 0, 2, 2],
    ["Acucar", 0, 5, 1.4],
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

#instanciando um armario
armario = Armario()

#Inserindo os produtos pre-definido no vetor de produtos
for aux in criarprodutos:
    produtos = armario.createProduct(aux[0], aux[1], aux[2], aux[3], produtos)

#Função atualizar valores de produtos
def update(produt):
    global produtos
    produtos = produt

#Função que envia os valores dos produtos
def sendValue():
    return produtos

#Função que enche
def fullValue(produt):
    for i in range(len(produt)):
        produt[i].atual = criarprodutos[i][2]
    
    update(produt)

#Função que esvaziar
def emptyValue(produt):
    for i in range(len(produt)):
        produt[i].atual = criarprodutos[i][1]
    
    update(produt)

#Função que deixa meio cheio
def halffullValue(produt):
    for i in range(len(produt)):
        produt[i].atual = criarprodutos[i][2]/2
    
    update(produt)

#Consumir parte do produto
def consume(produt, nomeProduto, porcentagem):
    for aux in produt:
        if aux.nome == nomeProduto:
            aux.atual *= (100-porcentagem)/100

    update(produt)
