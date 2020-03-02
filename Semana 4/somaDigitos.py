numero = int(input("Digite um número inteiro:"))
soma = 0
while (numero > 0):
    resto = numero % 10
    numero = (numero- resto)/10
    soma = soma + resto

print(soma)