# correção da somativa
# exercicio 1
# print("registro de veiculo")
# modelo = input("qual é o modelo do veiculo? ")
# placa = input("qual a placa do veiculo? ")
# print(f"veiculo {modelo} de placa {placa} registrado no sistema . boa viagem! ")

# exercico 2
# print("calculo de autonomia")
# tanque = float(input("qual é a capacidade de seu tanque em litros "))
# consumo = float(input("digite o consumo medio por caminhão em km/l "))

# total = tanque / consumo 
# print(f"seu caminhão pode percorrer {total:.2f} em km/l")
# print("seu caminhão pode percorrer", round(total,2),"em km/l")

# exercicio 3
# print("conversor de moeda(frente internacional)")
# valor_reais= float(input("qual será o valor em reais que será convertido? "))
# taxa_dolar=float(int("qual é o valor da taxa em dolar em reais? "))
# total = valor_reais / taxa_dolar
# (print(f"o valor total convertido é {total:.2f}"))

# exercicio4

# print("media de entrega")
# tempo1= int(input("qaul foi o tempo para concuir a rota 1 em hora "))
# tempo2= int(input("qaul foi o tempo para concuir a rota 2 em hora "))
# tempo3= int(input("qaul foi o tempo para concuir a rota 3 em hora "))
# media = (tempo1+tempo2+tempo3)/3
# print(f"a media {media:.2f} de tempo das entregas")

# exercicio 5
# peso = float(input("Qual é o peso do seu caminhão? "))
# if peso <= 10:
#     print("Carga Leve")
# elif peso <=25:
#     print("Carga Padrão")
# else:
#     print("ALERTA: Excesso de Peso!")

# exercicio 6
# print("classificador de destino")
# print("regiões = N - norte, S - sul, qualquer outra para internacional")
# regiao=input("inserir o codigo da regiao : ").lower()
# if regiao == "N".upper() or regiao == "n".lower():
#     print("região norte")
# elif regiao == "S".upper() or regiao == "s".lower():
#     print("região sul")
# else:
#     print("região internacional")

# exercicio7
# print("liberação de saida")
# checklist = input("o checklist foi concluido ? [concluido ou não concluido] ")
# motorista=input("o motorista fo indentificado? [sim ou não] ")
# if checklist == "concluido" and motorista == "sim":
#     print("veiculo autorizado a iniciar a rota")
# else:
#     print("veiculo NÃO autorizdo a iniciar a rota . verificar checklist e identificação do motorista")

# exercicio 8 

# total = int(input("total de entregas:"))
# atrasos = int(input("entregas com atraso: "))
# if atrasos > total *0.1:
#     print("necessario otimizar rotas")
# else:
#     print("Logística Eficiente")

# exercicio 9 
# print("variação de calibragem")
# pressao = float(input("digite a pressão dp pneu em PSI..."))
# if 100 <= pressao <=110:
#     print("dentro do padrão")
# elif pressao < 100:
#     print("abaixo do recomendado")
# else:
#     print("acima do recomendado")

# exercicio 10 
# print("contagem de embarco")
# import time
# for contagem in range(5,0,-1):
#     time.sleep(1)
#     print(contagem)
# print("PORTÃO TRANCADO!")

# exercicio 11

# print("somatorio de frete (acumulador)")
# while True:
#     valor=float(input("valor do frete: "))
#     if valor == 0:
#        total+=valor
#        print(f"total acumulado {total} do frete")
# print("F I M ")


# VERSAO 2 
# print("somatorio de frete (acumulador)")
# faturamente_total=0
# valor_frete= -1
# while valor_frete !=0
#     valor_frete= float(input("valor do frete ou 0 para encerrar"))
#     faturamente_total +=valor_frete
#     print(f"faturamento acumulado : R$ {faturamento_total}")
# print("calculo executado com sucesso")

# print("somatorio de frete (acumulador) versao 3")
# b=0
# while True:
#     t=int(input("vaor frete"))
#     c=int(input("quer continuar s/n"))
#     b+=t
#     if c == "s":
#         continue
#     else:
#         break
#  print(f"faturamento total{b} acumalado")

# exercicio 12
# print("monitoramento de frote")
# maior_km=0
# for frota in range(1,6):
#     km= float(input(f"digite a quilometragem do veiculo {frota}"))
#     if km > maior_km:
#         maior_km=km
# print(f"a maior quilometragem registrada é : {maior_km}km.")

# exercicio 13
# print("siteme de rasdtreamento")
# codigo_certo="track99"
# tentativas = 0
# max_tentativas = 3
# while tentativas < max_tentativas:
#     codigo_input=input("codigo de acesso patao rastreafor")
#     if codigo_input == codigo_certo:
#         print("acesso permitido.iniciando rastreamento")
#         break
# else:
#     tentativas += 1
#     print("Acesso negado")
#     if tentativas < max_tentativas:
#         print(f"tentativasrestantes: {max_tentativas}")
# else:
#  print(" bloqueado")