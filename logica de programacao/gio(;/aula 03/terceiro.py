# Lógicas e Decisões
# Se condições verdadeira
# Se condição ainda verdadeira porém com criterios
# Senao condiçao falsa
# if elif e else
# sinais de > < =


# Explo 1
# print("Verificar idade")
# idade = int(input("Digite sua idade"))

# if idade>= 18:
#     print("voce é maor de idade")
# elif idade >=16:
#     print("voce não é de maior porém pode votar")

# else:
#     print("voce não de maior")
    
# Exemplo 2
# Valores
# print("Checar valores")
# valor = int(input("Digite um valor "))

# if valor > 100:
#     print("Valores acima de 100")
#     print(" O valor é ", valor + 1)

# else:
#     print("Valores abaixo de 100")


# Exemplo 3
# Criar um algoritmo que permita escolher a opção que deseja
# print("Menu de opção")
# print("Escolha uma das opções")
# print("Filmes F e Séries S e X para Sair")

escolha = input("digite uma opção ")

if escolha == "F":
    print("Voce escolheu Filmes")
elif escolha == "S":
    print("Voce escolheu Séries")
else:
    print("Voce saiu do programa")
