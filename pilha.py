from no import No

class Pilha:
    def __init__(self):
        """
        inicialização do objeto que define a pilha e todas as funções que a compõem
        """
        self.topo = None
        self._size = 0

    def push(self, elemento):
        """
        insere elementos na pilha

        :param elemento: elemento a ser inserido
        """
        no = No(elemento)
        no.next = self.topo #registra a posição do elemento anterior
        self.topo = no
        self._size = self._size + 1


    def pop(self):
        """
        remove o elemento do topo da pilha

        :return: Elemento removido da pilha
        """
        if (self._size > 0):
            no = self.topo
            self.topo = self.topo.next
            self._size = self._size - 1
            return no
        raise IndexError("A pilha esta vazia")


    def peek(self):
        """
        visualizar o elemento do topo da pilha

        :return: Valor do elemento
        """
        if (self._size > 0): return self.topo.value
        raise IndexError("A pilha esta vazia")


    def __len__(self):
        """
        retorna o tamanho a pilha

        :return: Tamanho atual da pilha
        """
        return self._size


    def __repr__(self):
        """
        representação do objeto, mostra os elementos do objeto \n
        conforme definido na função
        :return:
        """
        r = ""
        pointer = self.topo
        while(pointer):
            r = r + str(pointer.value) + "->"
            pointer = pointer.next
        return r


    def __str__(self):
        """
        converte em strint, é chamado quando usa o print
        :return:
        """
        return self.__repr__()