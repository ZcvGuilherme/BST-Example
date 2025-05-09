# inserir uma lista de valores
# o primeiro valor da lista é a raiz
# comparar 
# 



class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None
    def buscar(self, value):
        return self.__buscar_recursivo(self.raiz, value)
    
    def __buscar_recursivo(self, node, value):
        if node is None:
            return None
        if value == node.valor:
            return node
        elif value < node.valor:
            return self.__buscar_recursivo(node.esquerda, value)
        else:
            return self.__buscar_recursivo(node.direita, value)
        
    def inserir(self, valor):
        self.raiz = self.__inserir_recursivo(self.raiz, valor)
    def __inserir_recursivo(self, node, valor):
        if node is None:
            return Node(valor)
        if valor < node.valor:
            node.esquerda = self.__inserir_recursivo(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self.__inserir_recursivo(node.direita, valor)
        return node

    

arvore = BST()

arvore.inserir(10)
arvore.inserir(15)
arvore.inserir(30)
arvore.inserir(45)
arvore.inserir(5)
arvore.inserir(12)
arvore.inserir(70)
arvore.inserir(23)
arvore.inserir(35)
arvore.inserir(1)


resultado = arvore.buscar(35)

if resultado:
    print("valor encontrado: ", resultado.valor)
else:
    print("não encontrado")