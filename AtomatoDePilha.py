from pilha import Pilha

lista = input("Escreva uma palavra ou frase: ")

palavras = lista.split()
palindormo = 0

def isPalindromo(wr):
    tam = len(wr)
    fim = "."
    mid = (tam//2) + (tam%2) #define o meio da palavra
    pilha = Pilha()
    pilha.push(fim)

    if (tam < 3):return False

    for i in range(tam):
        if i < mid-1:
            pilha.push(wr[i])
        elif (i == mid-1):
            continue
        else:
            x = pilha.peek()
            if (x == wr[i]):
                pilha.pop()

    return (pilha.peek()==fim)

quant = 0
saida=""

for w in palavras:
    p = isPalindromo(w)
    if p:
        quant =+ 1
        saida = saida + str("["+w+"] ")
    else:saida = saida + w + " "

print("Tem {0} palindromo".format(quant))
print(saida)

"""

def isPrimo(n):
    for _ in range(2,n):
        if _>=n:return True
        elif n%_ < 1:return False
    return True


for i in range(2,1000):
    x=isPrimo(i)
    if x:
        print(i)
"""