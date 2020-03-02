Xponto1=int(input("Entre com a coordenada X do primeiro ponto: "))
Yponto1=int(input("Entre com a coordenada Y do primeiro ponto: "))

Xponto2=int(input("Entre com a coordenada X do segundo ponto: " ))
Yponto2=int(input("Entre com a coordenada Y do segundo ponto: "))

Difx = (Xponto1 - Xponto2)**2 
Dify = (Yponto1 - Yponto2)**2 
distancia = (Difx + Dify)**(1/2)

if distancia > 10:
    print("longe")
else:
    print("perto")