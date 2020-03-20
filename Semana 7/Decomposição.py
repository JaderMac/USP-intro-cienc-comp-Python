num = int(input("Entre com um número inteiro: "))
fator=2
multi=0
while num>1:
    while num%fator ==0:
        multi = multi+1
        num = num/fator
    if(multi>0):
        print("Fator:",fator,"Multiplicidade:",multi)
    fator = fator+1
    multi = 0