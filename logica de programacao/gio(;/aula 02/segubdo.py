# Funções são blocos de código reutilizáveis
# O "f" no Python, usado antes das aspas de uma string (ou formatted string literal). Ele informa ao python que
#  a string contém expressões entre chaves{} que devem ser avaliados em tempo de execução e substituídas pelos seus valores reais.
# def saudacao(nome):
#     return f"Olá,{nome}!"
# mensagem= saudacao ("Maria")
# print(mensagem)
# def age (idade):
#     return f"Olá,{idade}!"
# mensagem= age("16")
# print(mensagem)

def boas_vindas(nome,cargo):
    print(f"Olá,{nome}!VocÊ é o novo {cargo}.")
boas_vindas("Ana", "Desenvolvedora")
boas_vindas("Carlo" , "Gerente")
boas_vindas("Bruno","Professor")

# Conversões
nome= input("nome:")
idade=int(input("sua idade:"))# converte texto para inteiro
print(f"{nome} tem{idade}anos")
