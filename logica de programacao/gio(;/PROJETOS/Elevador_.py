# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar. 


print("Olá, vocÊ está no Elevador da Gica")
an_atual = 0

while True:
    try: 
        
        an_atual = int(input(f"Olá, que andar você está ? "))
        an_desej = int(input(f"Qual andar deseja ir ? ")) 
        an_atualw = input(f" Irá Subir ou Descer ?  ")
        

        if an_atualw.lower() == ( "subir"):
            print(f"O Elevador subirá para o Andar {an_desej}")
        elif an_atualw.lower() == ("descer"):
            print(f"O Elevador descerá para o Andar {an_desej}")
        else:
            print("E-R-R-O, digíte 'subir' ou 'descer' ")


            if an_desej == 0:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 1:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 2:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 3:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 4:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 5:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 6:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 7:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 8:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 9:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            elif an_desej == 10:
                print(f"Vamos {an_atualw} para o Andar {an_desej} ")
            else:
                print(f"E-R-RO, Digíte o número do Andar desejado ")

            quant_pes = int(input(f"Quantas pessoas vão estar no Elevador ? {quant_pes}"))
            if quant_pes == ("1,6"):
                print(" OK,")
            elif quant_pes >= 5:
                print("!! LIMITE DE PESSOAS ULTRA PASSADO !!")

    except ValueError:
        print("Finalizando")