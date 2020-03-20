num=1
while(num!=0):
    num = int(input("Digite o valor de n: "))
    t=num
    fat=1
    while(num>0):
        fat=fat*num
        num = num-1    
    print(fat)
    if t<0:
        break
    num=1

