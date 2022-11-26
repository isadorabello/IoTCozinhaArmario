import json
class ListaCompra(object):

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
        count = 0
        for aux in produtos:
            if aux.atual <= aux.max*.3:
                count += 1
                for k, v in self.listaCompra.items():
                    if v == "":
                        self.listaCompra[k] = aux.nome
                        break
        
        for x in range(count+1, len(self.listaCompra)+1):
            aux = "Item" + str(x)
            self.listaCompra[aux] = ""