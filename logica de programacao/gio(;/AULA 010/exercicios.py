# tratamento de erros e depuração
# try e except são usados para lidar com erros de forma controlada, evitando que o programa quebre. O código dentro do bloco try é executado normalmente, mas se ocorrer um erro, o controle é passados para o bloco excep, onde podemos lidar com a situação asituação de forma apropriada.

# try: 
#     numero = int(input("Digite um numero :"))
#     resultado = 10 / numero
#     print("O resultado é :" , resultado)

# except ValueError:
#     print("Erro: Você deve digitar um numero válido. ")

# except ZeroDivisionError:
#     print("Erro: não é possível dividir por zero.")

# except KeyboardInterrupt:
#     print("\n Programa interrompido ")

# except TypeError:
#     print("Erro: Tipo de dado inválido")

# except Exception as erro:
#     print("Erro inesperado:",erro)


# Exercicio 1
#  escreva um programa que solicite ao usuario calcule a média de trÊs números. O programa deve lidar com possiveis erros, como a entrada de valores não números ou a divisão por zero.

# try:
#     nu1 = float(input("Digite o primeiro numero "))
#     nu2 = float(input("Digite o terceiro numero "))
#     nu3 = float(input("Digite o terceiro numero "))

#     media = (nu1 + nu2 + nu3) / 0
#     print(f"O resultado da média é: {media}")

# except ValueError:
#     print("Erro: Você deve digitar um numero válido. ")

# except ZeroDivisionError:
#     print("Erro: não é possível dividir por zero.")

# except KeyboardInterrupt:
#     print("\n Programa interrompido ")

# except TypeError:
#     print("Erro: Tipo de dado inválido")

# except Exception as erro:
#     print("Erro inesperado:",erro)


# exercicio 2
# explicaÇão de def: A palalavra-chave é usada para definir uma função em Python. Uma função é um, bloco de código reutilizável que realiza uma tarefa espeífica.
# return: Apalavra-chave "return" é usada para finalizar a execução de ums função e retornado pode ser usado posteriormente no código.

# def nome_da_funcao(paramentro1, paramentro2):
#   #cORPO da função (código que será executado)
#   resultado = parametro1 + parametro2
#   return resultado 

# Exemplo 1
# def saudacao(nome):
#     return f"Olá, {nome}!"
# print(saudacao("GICA.top_"))


# Exemplo 2
# def calcular_media(num1, num2, num3):
#     try:
#         media = (num1 + num2 + num3) /3
#         return media
#     except TypeError:
#         return "Erro: Todos os valores devem ser números."
#     except ZeroDivisionError:
#         return "Erro: Não é possível dividir por zero."
    
# print(calcular_media(10, 20, 30))

# Exercicio 3
# def valores():
#     print("Digite três valores: ")
#     a = int(input("Digite o primeiro valor: "))
#     b = int(input("Digite o segundo valor: "))
#     c = int(input("Digite o terceiro valor: "))
#     return a, b, c 
# print(f"O maior valor é: {max(valores())}")

#  Exemplo 4
# Calcule o dobro de um nummero fornecidos pelo usuario, tratado erros de entrda inválidas 
# def cacular_dobro():
#     try:
#         valor_digitado = int(input("Digite o valor que deseja :) "))
#         total_dobro = valor_digitado * 2
#         return total_dobro
#     except ValueError:
#         print("Digite um número válido")
# print(f"O calculo é : (calcular_dobro ())")
