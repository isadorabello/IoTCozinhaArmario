import time
from controller.armario import Armario
from controller.listacompra import ListaCompra

#instanciando um armario
armario = Armario()

#instanciando um lista de compras
listacompra = ListaCompra()

print(armario.initSensor())

print(armario.readSensor())
# armario.publish(armario.to_json(produto=produtos))
# time.sleep(1)
# listacompra.Calculate(produtos=produtos)