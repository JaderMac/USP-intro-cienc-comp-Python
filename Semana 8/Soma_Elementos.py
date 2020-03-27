def soma_elementos(lista):
    aux=0
    i=1
    while i <= len(lista):
        aux = aux + lista[i-1]
        i=i+1
    return aux