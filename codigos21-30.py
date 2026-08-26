#21 - Atividade

for numero in range(1,11):
    print (numero)

#22 - Atividade

numero =  10
while numero>= 1:
    print (numero)
    numero -=1

#23 - Atividade

numero = int(input("Digite um número: "))
for i in range(1,11):
    print(numero, "x", i, "=",numero * i)

#24 - Atividade

soma = 0
for numero in range(1,101):
    soma += numero
    print (f"A soma dos números de 1 a 100 é: {soma}")

#25 - Atividade

soma = 0
numero = float(input("Digite um número (0 para parar): "))
while numero != 0 :
    soma += numero
    numero = float(input("Digite um número (0 para parar): "))
    print (f"A soma dos números é: {soma}")

#26 - Atividade

contador = 0
for numero in range(1,51):
    if numero % 2 == 0:
        contador += 1
print (f"Existem {contador} números pares entre 1 e 50")

#27 - Atividade

for numero in range(1,31):
    if numero % 2 != 0:
        print (numero)

#28 - Atividade

positivos = 0
negativos = 0
for i in range(5):
    numero = float(input("Digite um número: "))
if numero > 0:
    positivos += 1
elif numero < 0:
    negativos += 1
    print (f"Positivos: {positivos}")
    print (f"Negativos: {negativos}")

#29 - Atividade

numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print (f"O fatorial de {numero} é {fatorial}")

#30 - Atividade

numero = int(input("Digite um número: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print (f"A soma é: {soma}")
