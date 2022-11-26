from conection.conection import Conection
import json

class ListaCompra(Conection):

    listaCompra_json = '{"Item1": "", "Item2": "", "Item3": "", "Item4": "", "Item5": "", "Item6": "", "Item7": "", "Item8": "", "Item9": "", "Item10": "", "Item11": "", "Item12": "", "Item13": "", "Item14": ""}'

    listaCompra = json.loads(listaCompra_json)

    def to_json(self):
        auxLista = '{'
        
        for k, v in self.listaCompra.items():
            auxLista += '"' + str(k) + '": "' + str(v) + '",'
        
        auxLista += '}'

        return auxLista

    def Publish(self, payload):
        self.client.publish(topic="Cozinha/ListaCompras", retain=True,qos=1, payload=payload)
    
    def Calculate(self, produtos):
        for aux in produtos:
            if aux.atual <= aux.max*.3:
                for k, v in self.listaCompra.items():
                    if v == "":
                        self.listaCompra[k] = aux.nome
                        break

        self.Publish(self.to_json())