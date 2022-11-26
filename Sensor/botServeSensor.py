from socket import *
from controller.armario import Armario
import time

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
# atribui a porta ao socket criado
serverSocket.bind(("", serverPort))
# aceita conexoes
# com no maximo um cliente na fil
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

#Criando um vetor de produtos vazio
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

#instanciando um armario
armario = Armario()

#Inserindo os produtos pre-definido no vetor de produtos
for aux in criarprodutos:
    produtos = armario.createProduct(aux[0], aux[1], aux[2], aux[3], produtos)

#Criando a função de enviar a leitura
def writeSensor(produtojson):
    connectionSocket.send(produtojson.encode())

def init():
    for i in range(len(produtos)):
        produtos[i].atual = i

#Recebendo as informações iniciais
msg = connectionSocket.recv(1024).decode()
if msg == "init":
    writeSensor(armario.to_json(produtos))
    init()

writeSensor(armario.to_json(produtos))