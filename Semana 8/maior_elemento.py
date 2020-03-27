def maior_elemento(temperaturas):
    maxima= -1000
    for temperatura in temperaturas:
        if temperatura >= maxima:
            maxima = temperatura
    return maxima