class listaordenada:
    def __init__(self):
        self.lista = []

    def adicionar(self, valor):

        for i in range(len(self.lista)):
            if self.lista[i] > valor:
                self.lista.insert(i, valor)
                return
        
        self.lista.append(valor)

    def printarli(self):
        print(self.lista)

lista = listaordenada()
lista.adicionar(6)
lista.adicionar(2)
lista.adicionar(7)
lista.adicionar(14)

lista.printarli()