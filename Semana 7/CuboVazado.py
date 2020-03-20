largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
vazio= ''
for i in range(altura):
    for j in range(largura):
        if(j == 0 or i == 0 or j == largura-1 or i == altura-1):
            vazio += '#'
            continue
        vazio += ' '
    vazio += '\n'
print(vazio)
