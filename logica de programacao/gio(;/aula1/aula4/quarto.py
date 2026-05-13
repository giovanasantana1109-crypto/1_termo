#1. olaço 'for' (repetições Determinadas)
# use o 'for' quando você sabe exaamente quantas vezes algo deve acontecer (com ler 10 sensores ou processar uma lista de peças ).PendingDeprecationWarning
# exemplo: relatório de produção diária
# imagene que você tem uma meta de produzir 5 lotes e quer numerar cada um:


# Exemplo 1
# for lote in range(1,6):
#     print(f"Processando lote número {lote...}")
#     print("Quantidade verificada.[OK]")
#     print("Produção do dia finalizada!")

# Exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b}foi...")

# exemplo 3
# # imagine o seguinte cenário, iremos produdiz 20 discos de vinil
# for y in range(21):
#     print(f"Foram produzidos {y} discos de vinil")
# print("Sequencia finalizada")


# exemplo 4
# pecas = ["Engrenagem","Eixo","Rolamento", "Parafuso","Martelo","Prego","Chave de Fenda"]
# itempecas = ["Cilindrica","Duplo","Cônica", "Prego" ,"Orelha","Redondo","Phill"]

# for item in pecas:
#     print(f"Item em estoque: {item} e {itempecas}")

# exemplo 5
# imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qaul opção você deseja e a partir da seleção ele os produtos

print("Qual opção você deseja para comer? ")
D=("Doce")
S=("Salgado")
opcao=input("Doce ou Salgado, digite 'D' para doce e 'S' para salgado ",)
if opcao== "D":
    print("Você escolheu a opção de doce e esses são o qeu temos disponiveis: ")
for opcao in range(1):
    d = print(f"Pudim,Paçoca,Goiabada")

for opcao in range(1):

    s =print(f"Coxinha, Empada,Esfirra ")











