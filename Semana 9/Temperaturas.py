def MinMax(temperaturas):
    print("A menor temperatura do mês foi:",minima(temperaturas),"C.")
    print("A maior temperatura do mês foi:",maxima(temperaturas),"C.")

def maxima(temperaturas):
    maxima= -1000
    for temperatura in temperaturas:
        if temperatura >= maxima:
            maxima = temperatura
    return maxima

def minima(temperaturas):
    minima= 1000
    for temperatura in temperaturas:
        if temperatura <= minima:
            minima = temperatura
    return minima

temperaturas = [10,12,23,1,32,32,12,25,21,35,20,18,19,13,12,10,13,13,29,12,23,13,7,13,27,25,23,17,12,23,15]

max=maxima(temperaturas)
min=minima(temperaturas)

MinMax(temperaturas)
