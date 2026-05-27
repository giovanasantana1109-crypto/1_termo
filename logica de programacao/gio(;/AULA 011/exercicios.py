# Interface Gráfica com Tkinter
#

# Os componentes principais (Widgets)
# Tk: Janela principal
# Label: é o texto a digitar = print
# Button : Botão clicável de evento 
# Entry: caixa de texto = input

# 0. Biblioteca 
import tkinter as tk
from tkinter import messagebox

# 1. Criar Janela
janela = tk.Tk()
janela.title("Minha Primeira Janela em GUI")
janela.geometry("800x400")

# 2. Criar função do botão 
def mostrar_mensagem():
    messagebox.showinfo("Sucesso", "Você clicou no botão (;")

# 3. Criar os componentes
lbl_Giovana_Landia = tk.Label(janela, text="Bem-Vindo a Minha Aula de Interface Grafica em Python", font=("Arial",14,"bold"))
lbl_Giovana_Lanndia = tk.Label(janela, text=" Giovana Futura Fisioterapeuta ", font=("Arial",12,"bold"))

btn_clique_ativar = tk.Button(janela, text="Clique Aqui (;", font=("Arial", 14), bg="#6bddc4", fg="White", command=mostrar_mensagem)
btn_clique_fechar = tk.Button(janela,text="Fechar Aplicativo", command=janela.destroy)
lbl_Giovana_Landia.grid(row=0, column=0, padx=10, pady=10)
btn_clique_ativar.grid(row=1,column=1,padx=15,pady=15)
lbl_Giovana_Lanndia.grid(row=0, column=1, padx=9, pady=3)

# 4. Como Posicionar os componentes na janela
# lbl_Giovana_Landia.pack(pady=5)#adicionar espaçamento
# btn_clique_ativar.pack(pady=10)
# btn_clique_fechar.pack(pady=15)


# 5.Rodar interface
janela.mainloop()