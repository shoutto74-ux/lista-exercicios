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
