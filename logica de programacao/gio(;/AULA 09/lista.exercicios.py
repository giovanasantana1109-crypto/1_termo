# Exercícios de Programação Python: "O Caça-Erros"

# exercicio 1

#  versão como erro

# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

#  versão corrigida

# 1. O problema da Idade
# idade = int(input("Digite sua idade "))
# if idade >= 18:
#     print("Você é maior de idade. ")

#  versão melhorada 

# idade = int(input("Digite sua idade "))
# if idade >= 18:
#     print("Você é faior de idade. ")
# elif idade <= 18:
#     print("Você é menor de idade. ")


# exercicio 2

#  versão como erro

# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")


#  versão corrigida

# nome =("Mariana")
# print(f"Seja Bem-Vinda {nome}! ")



#  versão melhorada

# nome = input("Qual é o seu nome? ")
# print(f"Seja bem-Vinda {nome} ! ")

# exercicio 3 

#  vesão com erro

# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")


#  versão corrigida
# numero = 10 
# if numero > 5 :
#     print(" O número é maior que cinco")
# else:
#     print("O número é menor ou igual a cinco")


#  versão melhorada 

# nume = int(input("Digite um número de 0 a 10? "))
# if nume >= 5:
#    print("O seu número é maior que cinco")
# elif nume <= 5:
#     print("Seu número é menor que cinco ")
# else:
#     print("ERRO: Você digitou algo errado. Tente novamente")

# exercicio 4

#  versão errada
# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")


#  versão corrigida
# usuario = ("aluno123")
# if usuario == "aluno123":
#     print("Login reakizado com sucesso.")


#  versão melhorada
# usuario = ("ALUNO123")
# if usuario == "ALUNO123":
#     print("Login do aluno realizado com sucesso !")

# exercicio 5

# versão erro
# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

# versão corrigida
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva! ")

# versão melhorada

# clima = input("Está chuvendo hoje? sim/não  ")

# if clima == "sim":
#     print("Está chuvendo, então leve guarda-chuva! ")
# elif clima == "não":
#     print("Está ensolarado, então não leve guarda-chuva :) ")
# else:
#     print("ERRO na sua resposta. A resposta só pode ser 'sim' ou 'não'")


# exercicio 6
# versão errada
# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# versão corrigida
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")


# versão melhorada
# pontos = int(input("Quantos pontos você fez na prova de português que a nota é de 0 à 100 ? "))

# if pontos <= 40:
#     print("Você ficou à abaixo da média, estude um pouco mais para a proxima prova ")
# elif pontos >= 60:
#     print("Ficou acima da média, continue assim ! O seu esforça vale apena :) ")
# elif pontos == 50:
#     print("Você ficou na média ")
# else:
#     print("ERRO, digite a nota que você tirou! ")

# exercicio 7

# versão errada

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")


# versão corrigida 
# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")


# versão melhorada
# nota = int(input("Qual foi sua nota de 0 á 10 em Biologia ? "))

# for nota in range(5, 8):
#     if nota  (5,6,7,8):
#         print("Aprovado")

# for nota in range(9,10):
#     elif nota (9,10):
# print("EXELÊNTE")

# for nota in range(0,4):

# elif nota  (0,1,2,3,4):
#     print("Você foi reprovado, irá precisar de recuperação")

# else:
#     print("ERRO, digite a sua nota de 0 à 10, por favor ! ")


