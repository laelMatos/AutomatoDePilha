class No:
    """
    Representa cada elemento de uma pilha \n
    (next) -  representa o elemento anterior \n
    (data) - o proprio elemento
    """
    def __init__(self, data):
        self.value = data
        self.next = None