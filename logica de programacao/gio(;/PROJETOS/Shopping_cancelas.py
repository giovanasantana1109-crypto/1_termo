# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

print("- - - BEM-VINDO AO ESTACIONAMENTO - - -")
forma_acesso= input("O veículo possui TAG ? (sim/não) ")

if forma_acesso == "sim":
    print("TAG foi identificada.")
    print("Acesso Liberado.")
elif forma_acesso == "não":
    input("Aperte o botão [ENTER] para imprimir o Ticket")
    print("Ticket emitido.")
else:
    print(" E R R O : ACESSO NÃO PERMITIDO !")

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

tempo = int(input("Quantas horas vocÊ ficara no estacionamento? "))
pagamento = print(" Deve ser pago ", tempo*12 , " para o estacionamento ")


# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída


print(f"Você esteve no Shopping por {tempo} horas e o valor a ser pago é de {pagamento}")
quan_t = input(" Você fez o pagamento por meio de Ticket ou TAG ?  Ticket/TAG")

if quan_t == "Ticket":
    print(f"Devolva o Ticket e faça o pagamento de {pagamento}")
elif quan_t == "TAG":
    print(f"A fatura a ser paga é de {pagamento}")
else:
    print("  E R R O ! Responda corretamente ! ")




# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código






















