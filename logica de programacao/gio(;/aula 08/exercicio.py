# tratamentos de erros e eceçõ~es

# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# resultado = valor1/valor2


# print(f"O resultado da divisão é: {resultado} ")
# o codigo acima pode gerar um errode divisão por zero se o usuario digita 0 para o segundo valor. para  o segundo valor, para tratar esse erro , podemos usar um bloco try-except:
# try:
#     valor1 = int(input(f"Digite o primeiro valor: "))
#     valor2 = int(input(f"Digite o primeiro valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")


# Exemplo 2: Tratamento de entrada inválida

# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro de valor: Por favor, digite um número inteiro válido.")

# Exemplo 3: Tratamento de múltiplas exceções
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de valor: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possível dividir por zero. {e}")

# Exemplo 4: Uso do bloco finally

# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de valor: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possível dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")


# exercicio 1; 
# crie um algoritimo que pergunte o seu nome e trate erro ao inserir o valor incorreto

try:
    nome1 = input("Qual é o seu nome : ")
except ZeroDivisionError:
    print("Erro: Não é possível somar zero ")
