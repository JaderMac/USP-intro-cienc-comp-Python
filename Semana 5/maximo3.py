def maximo(intA,intB,intC):
    if(intA>intB) and (intA>intC):
        return intA
    else:
        if intB>intC:
            return intB
        else:
            return intC