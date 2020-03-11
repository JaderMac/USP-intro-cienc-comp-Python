def Primo(numero):
    cont = 0
    i = 0
    while ((i<=numero) or (cont<2)):
        i=i+1
        x = numero%i
        if x==0:
            cont=cont+1
    if cont <= 2:
        primo = True
        return primo
    else:
        primo = False
        return primo

def maior_primo(numero):
    ind=numero
    while (ind>0):
        p=Primo(ind)
        if(p==True):
            return ind
            break
        else:
            ind=ind-1
  