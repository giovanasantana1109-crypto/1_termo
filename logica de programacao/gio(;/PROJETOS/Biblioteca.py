# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"
# Contexto: Você foi contratado para desenvolver o módulo de validação de
# empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados
# do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá
# cobrança de taxa de segurança.


# Regras de Negócio (O que o sistema deve fazer):
# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade Geral.




# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça
# ○ A Comunidade Geral pode ficar por até 7 dias de graça.



# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
# perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.





# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
# para a Comunidade Geral, apenas para Alunos.

import tkinter as tk
from tkinter import messagebox,ttk
#def biblioteca():
    # .get() serve para buscar o texto da caixa
    # nome_usuario = usuario_nome.get()
    # idade_usuario = usuario_idade.get()

    # if nome_usuario == "" and idade_usuario == "":
    #     messagebox.showwarning("Aviso", "Por favor difite seu nome e idade! :)")
    # else:
    #     messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! Parabéns pelos {idade_usuario} de vida :) ")


janela = tk.Tk()
janela.title("Biblioteca Digital")
janela.geometry("500x600")
janela.configure(bg="lightblue")



lbl_mensagem_usuario = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=1, column=0, pady=10, padx=10)

usuario_nome = tk.Entry(janela, font=("Arial", 12))
usuario_nome.grid(row=2,column=0,pady=10,padx=10)


combo_classificacao_do_usuario = tk.ttk.Combobox(janela, values=["Aluno","Comunidade Geral"], width=30)
combo_classificacao_do_usuario.grid(row=4, column=0, pady=20, padx=20)

lbl_tipo_d_usuario = tk.Label(janela, text= ("Que Tipo de usuario é o seu"))
lbl_tipo_d_usuario.grid (row=3, column=0, pady=20, padx=20)



combo_livros = tk.ttk.Combobox(janela, values=["Alice no Pais das Maravilhas","Pequeno Príncipe", "Eu e esse meu coração ", "Todo esse tempo","Quem mexeu no meu queijo?", "A Biblioteca da Meia-Noite: 1"], width=30)
combo_livros.grid(row=6, column=0, pady=20, padx=20)

lbl_livros = tk.Label(janela, text= ("Título do Livro"))
lbl_livros.grid (row=5, column=0, pady=20, padx=20)


combo_categoria_do_livro = tk.ttk.Combobox(janela, values=["Comum","Raro"], width=30)
combo_categoria_do_livro.grid(row=8, column=0, pady=20, padx=20)

lbl_categ = tk.Label(janela, text= ("Categoria do Livro"))
lbl_categ.grid (row=7, column=0, pady=20, padx=20)


combo_dias = tk.ttk.Combobox(janela, values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14"], width=30)
combo_dias.grid(row=10, column=0, pady=20, padx=20)

lbl_dias = tk.Label(janela, text= ("Dias Solicitados"))
lbl_dias.grid (row=9, column=0, pady=20, padx=20)








janela.mainloop()
    