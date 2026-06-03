import tkinter as tk
from tkinter import messagebox,ttk

def bemvindo():
    # .get() serve para buscar o texto da caixa
    nome_usuario = usuario_nome.get()
    idade_usuario = usuario_idade.get()

    if nome_usuario == "" and idade_usuario == "":
        messagebox.showwarning("Aviso", "Por favor difite seu nome e idade! :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! Parabéns pelos {idade_usuario} de vida :) ")

def segunda_janela():
    segunda_janela = tk.Toplevel(janela_bemvindo)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("500x500")

    lbl_segunda_janela = tk.Label(segunda_janela, text="Bem-Vindo a Segunda Janela :)" )
    lbl_segunda_janela.grid(row=0, column=0, pady=10, padx=10)

# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações do Usuário")
janela_bemvindo.geometry("500x500")

# Componentes
# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrocos", "Egito", "Escócia"], width=30)
combo_nivel.grid(row=25, column=0, pady=20, padx=20)

# Labels
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem_pusuario = tk.Label(janela_bemvindo, text = ("Digite sua idade"))
lbl_mensagem_pusuario.grid (row=3, column=0, pady=10, padx=10)

lbl_mensagem_nusuario = tk.Label(janela_bemvindo, text=("Qual é o seu país") )
lbl_mensagem_nusuario.grid (row=24, column=0, pady=20, padx=20)

# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12))
usuario_nome.grid(row=1,column=0,pady=10,padx=10)
usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12))
usuario_idade.grid(row=4,column=0,pady=10,padx=10)

# Botão

btn_enviar_mensagem2 = tk.Button(janela_bemvindo, text="Enviar Mensagem", bg="#a06bdd", fg="White" ,command=bemvindo)
btn_enviar_mensagem2.grid(row=28, column=0, pady=27, padx=27)

btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela",bg="#dd6b84", fg="White" , command=segunda_janela)
btn_segunda_janela.grid(row=34, column=0, pady=20, padx=20)

btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela",bg="#d06bdd", fg="White" , command=janela_bemvindo.destroy)
btn_fechar_janela.grid(row=37, column=0, pady=20, padx=20)


# Rodar interface
janela_bemvindo.mainloop()