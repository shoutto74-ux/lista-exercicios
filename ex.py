#1 - Atividade

nome = input ("Digite seu nome: ")
print (f"Olá, {nome}! Seja bem vindo(a)! ")

#2 - Atividade

numero = int(input("Digite um número inteiro: "))
dobro = numero *2
print (f"O dobro é: {dobro}")

#3 - Atividade

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print (f"A soma é: {soma}")

#4 - Atividade

idade = int(input("Digite sua idade: "))
idade_futura = idade + 10
print (f"Daqui a 10 anos, você terá : {idade_futura} anos")

#5 - Atividade

numero = float(input("Digite um número: "))
quadrado = numero **2
print (f"O quadrado é: {quadrado}")

#6 - Atividade

salario = float(input("Digite o salário: "))
novo_salario = salario *1.10
print (f"O novo salário com o aumento é: {novo_salario}")

#7 - Atividade

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius *9/5) + 32
print (f"A temperatura em Fahrenheit é: {fahrenheit}")

#8 - Atividade

numero = float(input("Digite um número: "))
metade = numero / 2
print (f"A metade do número é: {metade}")

#9 - Atividade

comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
area = comprimento * largura
print (f"A área do terreno é: {area}")

#10 - Atividade

numero = int(input("Digite um número: "))
antecessor = numero -1
sucessor = numero +1
print (f"O antecessor é: {antecessor}")
print (f"O sucessor é: {sucessor}")

#11 - Atividade

numero = float(input("Digite um número: "))
if numero >0:
    print ("O número é positivo")
elif numero <0:
    print ("O número é negativo")
else:
    print ("O número é zero")

#12 - Atividade

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print ("O número é par")
else:
    print ("O número é ímpar")

#13 - Atividade

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print ("Você é maior de idade")
else:
    print ("Você é menor de idade")

#14 - Atividade

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print ("Aluno aprovado!")
else:
    print ("Aluno reprovado!")

#15 - Atividade

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
maior_numero = max (numero1,numero2,numero3)
print (f"O  maior número é: {maior_numero}")

#16 - Atividade

numero = int(input("Digite um número inteiro: "))
if numero % 5 == 0:
    print ("O número é múltiplo de 5")
else:
    print ("O número não é múltiplo de 5")

#17 - Atividade

senha = input("Digite a senha: ")
if senha == "1234":
    print ("Senha correta!")
else:
    print ("Senha incorreta!")

#18 - Atividade

numero = float(input("Digite um número: "))
if 10 <= numero <= 20:
    print ("Esse número está entre 10 e 20")
else:
    print ("Esse número não está entre 10 e 20")

#19 - Atividade

preco = float(input("Digite o preço do produto: "))
if preco > 100:
    preco = preco *0.95
print (f"O preço final é: {preco}")

#20 - Atividade

ano = int(input("Digite um ano desejado: "))
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print (f"{ano} é ano bissexto")
else:
    print (f"{ano} não é ano bissexto")

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