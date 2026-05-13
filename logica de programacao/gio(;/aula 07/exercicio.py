# Clean code - aula 7
# para que usar?
# Como usar?
# print("Clean Code - Aula 7")
# aula = 7
# print(f"Estamos na aula {aula} de Clean Code")




# print("Perfil de Gamer")
# nick=input("Qual é o seu nick no jogo? ")
# nivel=int(input("Qual nível você alcançou no jogo até agora? "))
# print(f"O jogador {nick} está no nível {nivel} e ponto para a partida! ")




# print("Calculadora de Mesada ")
# semana=int(input("Quanto de mesada você ganha por semana? "))
# no_final_do_mes = semana*4
# print(f"No final do mês você estará ganhando  {no_final_do_mes} de mesada")




# manioulação de arquivos e texto
# manipular_texto= " Python é Muito legal! "
# print(manipular_texto.strip().upper())#"PYTHON"
# print(manipular_texto.strip().lower())#"python"
# print(manipular_texto.strip().startswith("A"))#"Começar com Letra inicial"
# print(manipular_texto.strip().capitalize)#"Letra Inicial"
# print(manipular_texto.strip().title())#"Titulo"
# print(manipular_texto.strip().replace(" ","_"))#"Preencher vazios"
# print(manipular_texto.strip().split())#"Separar palavras"




# Exercicio 1
# Crie um programa que peça ao usuario para inseserir uma frase e, em seguidad exiba a frase com os seguintes transformações:
# Deixe o texto em Letras minusculas

# frase_usuario=input("Digite uma frase: ")
# print(frase_usuario.strip().lower())



# exercico2
# Escrevendo
# with open("notas.txt","w", encoding="utf-8") as texto:
#     texto.write("Estudar python hoje! ")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estamos evoluindo.")



# lendo
# with open("notas.txt","r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)



# exemplo 1
# crie um programa que leia o conteudo de um arquivo de texto e conte quantas vezes a palavra "python" aparece no arquivo.exiba o resultado para o usuario

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON") # Contar a palavra "Python"
#     contagem = conteudo.lower().count("python")
#     print(f"A contagem de palavras {contagem} é de...")







# Interação com o sistema operacional
# import os 
# importa o módulo os para inretagir com o sistema opecional
# onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# Criar pastas
# import os
# os.mkdir("Gio")

# Renomear pastas
# import os  
# os.rename("Minha_Pasta","Gio")

# apagar pastas
# os.rmdir("Nova_Pasta")

# 
