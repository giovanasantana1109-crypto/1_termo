# Revisão de conteudo
# print = "função de saída de dados para o console"
# input = "Função de entrada de dados do usuario via teclado"
# if = "Estrutura de decisão para executar código condicionalmente "
#   elif = " Combinação de else + if para verificar múltipla condições"
#   else = "Parte opcional de um if que executa código quando a condição do if é falsa"
# for =" Laço de repetição para iterar sobe uma sequência de elementos "
# while = "Laço de repetição para executar código enqunto um acondição fo verdadeira"
# operadores matematicos : +,-,*,/,//,%,**
# operadores de comparação:==,!=,>,<,>=,<=
# variavel = " exemplo de variável para armazenar dados"
# print(variavel)

# Exemplo 1: com print e input
# nome = input ("Digite seu nome: ")
# print(f"Olá, {nome}! Bem-vindo á aula de Python para Desenvolvimento de Sistemas!")

# Exemplo 2: com if, elif e else (sao condicoes impostas pelos codigos)
# nota = float(input("Digite a nota do aluno: "))
# if nota >=7:
#     print("Aluno aprovado!")
# elif nota >= 5:
#     print("Aluno em recperação.")
# else:
#     print("Aluno reprovado.")


#  exemplo 3: com for
# materiais = ["metais" , "plastico", 'vidro']
# for material in materiais:
#     print(f"Processando material: {material}")
#     print(f"Material{material} processado com sucesso!")
# print("Fim do processamento de materiais")
 
# 2. Laço While (Repetições Indeterminadas)
# Use o while quando você não sabe quando vaiparar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).

# Exemplo: Monitor de temperatura estiver segura
# import time
# temperatura = 25
# while temperatura < 100:
#     print(f"Temperatura atual: {temperatura} °C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3  #Simulando o aquecimento da maquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor..")


# Lista de temperatura lidas pelo sensor po minuto
# leituras = [70,75,82,98,110, 85,80]
# for temp in leituras:
#     while temp > 100:
#         print(f"CRÍTICO:{temp} °C detectados! Acionado parada dw em emergência")
#         break #  o loop para aqui NÃO lê os proximos valores (81 e 80)
#     print("Sistemas desligado.Aguardando manutenção")


# produçao de peças com controle de material usando continue
# materiais = ["metal", "metal", "plasticos","metal","vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso : Peça de {peca} detectada, Desviando para descarte...")
#         continue
    # pular o restante do codigo abaixo e vai para s proxima peca
    # este cotigo so roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")
# print("Fim do lote de produção")

# exercicio 1
# tente criar um codigo  que de 1 a 10 , mas use o continue para não imprimir o numero 5 (simulando uma falha de sensor especifica no item5)

# numeros = ["1","2","3", "4", " Ove uma falha no sensor 5","6","7","8","9","10"]
# for nn in numeros:
#     print(f"Olha os numerosa aqui ó {nn} (; ")
# print(f" Prontinho ó ")

# Exercicio 2
# simule um semaforo  com parada para cada cor . determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor . use o continue para pular a cor amarela (simulando um semafaro com defeitoqu nao acende a luz amarela)
# import time
# print("Semáfaro da gijoca canhota minhoca")
# color = [f"RED,joaninha da moranga, LIGADO (;"," ~~","YELLOW,abelhudo, ESTÁ COM FALHA!  ):","~~","GREEN,alface com abacate,LIGADO (;","~~"]
# for cor in color:
#     print(f"{cor}   ")
#     time.sleep(2)
# print( f"Semáforo da gijoca canhota minhoca ESTA DESLIGA AGORA /:")

#  # exercicio 3 Soma de carga de energia (for)
# # uma fabrica tem 5 maquinas. peça ao usuario (via input dentro do loop) o consumo em kwh de cadauma das 5 maquinas. ao final do loop , o programa de exibir o consumo total da fabrica.

# print("~ Soma de carga de Energia ~ ")
# consumo_total = 0
# for A in range(1,6):
#     consumo = float(input(f"Digite o consumo da maquina {A} (em KWh: )"))
#     consumo_total += consumo

# print(f"\n0 consumo total da fábrica é:{consumo_total:.2f} KWh")

# Exerciocio 4 Identifica de Peças Defeituosas (for +if)
# percorra uma lista de medidas de peças:
# medidas = [50.1,49.8,52.0,50.0,48.5]
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais
# use um for para ler a lisa e, para cada peça , diga se ela está "Aprovada" ou "rejeitada"

# print("Unidade de Indentificação de Peças da Canjica (; ")
# medid =  [50.1,49.8,52.0,50.0,48.5]
# a =(float (input("Qual é a medida da sua peça? ")))
# if medid <= 50.0:
#     print(" Não está no padrão de qualidade")
# elif medid >= 50.0:
#     print("Está dentro do padrão")
# else:
#     print("Fim! ")
 
# exercicio 5 - uma balança industrial está pesando um lote de 6 sacos de insumos. o peso ideal de cada saco é 50 kg, mas o sistema aceita variações 
# crie um programa que peça ao usuario o peso de cada (via input detro do loop ) e, para cada um , informe se ele está "dentro do limite" (entre 48 kg e 52kg)ou " fora do limite" . no final , exiba quantos sacos est~so dentro do limite.

# print("Balança Industrial   ")
# peso_total = 0
# for A in range(1,7):
#     peso =float(input(f"Digite o peso do saco {A} " ))
# if 48 <= peso <= 52:
#     print("Dentro do limite")

# else:
#     print("Fora do limite")
# print(f"\nTotal de sacos dentro do limite é:  {peso_total}")


# o desafio: gestão de ciclo termico 
# voce deve criar um programa que















