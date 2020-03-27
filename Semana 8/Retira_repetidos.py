#lista2 = [10,12,23,1,32,32,12,25,21,35,20,18,19,13,12,10,13,13,29,12,23,13,7,13,27,25,23,17,12,23,15]

lista2 = [2, 4, 2, 2, 3, 3, 1]

def remove_repetidos(lista):
    aux = lista[:]
    saida = []
    i=1
    i2=1

    while i <= len(lista):
        while i2 <= len(aux):
            if lista[i-1] != aux[i2-1]:
               saida.append(lista[i-1])
            i2=i2+1
        i=i+1

    return saida

print(remove_repetidos(lista2))

