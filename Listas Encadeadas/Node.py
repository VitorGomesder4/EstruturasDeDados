#Criação de um nó simples
class Node:
    def __init__(self, item):
        self.item = item
        self.prox = None

class lista_encadeada:
    def __init__(self):
        self.head = None
    
    def append(self, item):
        newnode = Node(item)
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while lastnode.prox:
                lastnode = lastnode.prox
            lastnode.prox = newnode
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.item, end=" -> ")
            current_node = current_node.prox
        print("None")

Lista_encadeada = lista_encadeada()
Lista_encadeada.append(10)
Lista_encadeada.append(20)
Lista_encadeada.append(10)
Lista_encadeada.print_list()