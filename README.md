# 🌳 Árvore de Busca Binária (BST) em Python

Este projeto busca implementar de maneira simples uma **Árvore de Busca Binária** em Python, com operações básicas de inserção e busca de valores

## 📌 Funcionalidades
- Inserção em árvores
- Busca por valores na árvore
- Impressão na tela do resultado

## 🧠 Como funciona

1. O primeiro valor inserido se torna a raiz da árvore.
2. Valores menores que o nó atual são inseridos à esquerda.
3. Valores maiores são inseridos à direita.
4. A busca percorre a árvore utilizando recursividade comparando o valor procurado com os nós.

## 🧪 Exemplo de uso
No código fonte têm o seguinte exemplo:
``` python
arvore = BST()

# Inserindo valores
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

# Buscando um valor
resultado = arvore.buscar(35)

if resultado:
    print("valor encontrado: ", resultado.valor)
else:
    print("não encontrado")

```

Em linhas gerais, o código inicializa uma classe BST, logo após se insere os valores desejados, e após a inserção, se faz a busca, que caso seja encontrado o valor, o resultado é printado, senão uma mensagem de erro.

#🚀 Como executar
1. Copie o código para um arquivo Python, como ```bst.py```
2. Execute com Python 3:
3. ``` bash
   python bst.py
   ```
