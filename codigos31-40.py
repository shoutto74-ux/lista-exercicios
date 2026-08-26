#31 - Atividade

numeros = [10,20,30,40,50]
for numero in numeros:
    print (numero)

#32 - Atividade

numeros = []
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
print (numeros)

#33 - Atividade

numeros = [10,25,7,42,18]
maior = max(numeros)
print (f"O maior valor é: {maior}")

#34 - Atividade

numeros = [10,25,7,42,18]
menor = min(numeros)
print (f"O menor valor é: {menor}")

#35 - Atividade

numeros = [10,20,30,40,50]
soma = sum(numeros)
print (f"A soma dos elementos é: {soma}")

#36 - Atividade

numeros = [10,21,32,45,50]
pares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
print (f"A quantidade de números pares é: {pares}")

#37 - Atividade

numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero % 2 == 0:
        print (numero)

#38 - Atividade

numeros = [1,2,3,4,5]
numeros.reverse()
print (numeros)

#39 - Atividade

numeros = [10,20,30,40,50]
numero = int(input("Digite um número para procurar: ")) 
if numero in numeros:
    print ("O número existe na lista")
else:
    print("O número não existe na lista")

#40 - Atividade

numeros = [30,10,50,20,40]
numeros.sort()
print (f"A lista em ordem crescente é: {numeros}")
