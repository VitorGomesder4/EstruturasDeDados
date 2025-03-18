class treeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

n1 = treeNode(10)
n2 = treeNode(15)
n3 = treeNode(20)

n1.esq = n2
n1.dir = n3

print(n1.valor, n1.esq.valor, n1.dir.valor)