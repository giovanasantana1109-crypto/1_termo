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
4. Esquecimento Fatal
usuario = "aluno123"
if usuario == "aluno123"
print("Login realizado com sucesso.")


#  versão corrigida
# usuario = ("aluno123")
# if usuario == "aluno123":
#     print("Login reakizado com sucesso.")


#  versão melhorada


