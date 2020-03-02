A=int(input("Insira o valor de A : "))
B=int(input("Insira o valor de B : "))
C=int(input("Insira o valor de C : "))
delta = ((B**2)-4*A*C)

if(delta == 0):
    Raiz1 = (-B+(delta)**(1/2))/(2*A)
    print("a raiz desta equação é",Raiz1)   
elif delta < 0:
    print("esta equação não possui raízes reais.")
else:
    Raiz1 = (-B+(delta)**(1/2))/(2*A)
    Raiz2 = (-B-(delta)**(1/2))/(2*A)
    if Raiz1 > Raiz2 :
        print("as raízes da equação são",Raiz2,"e",Raiz1)
    else:
        print("as raízes da equação são",Raiz1,"e",Raiz2)
