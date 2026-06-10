# Foco: print, input, operações matemáticas e f-strings

# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox,ttk

# # Criar Janela
# janela = tk.Tk()
# janela.title("Janela da Somativa")
# janela.geometry("800x400")

# #  Criar função do botão
# def turno():
#     # .get() serve para buscar o texto da caixa
#     nome_usuario = usuario_nome.get()
#     turno_top = combo_nivel.get()

#     if nome_usuario == "" and turno_top =="":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e turno! :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Operador(a){nome_usuario} registrado no Turno {turno_top}. Boa jornada!")

# #  Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-Vindo ao Descubra Quem é o operador", font=("Arial",14,"bold"))
# lbl_titulo.grid(row=0, column=2, padx=10, pady=10)


# # Labels
# lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:")
# lbl_nome_usuario.grid(row=3, column=0, pady=10, padx=10)

# lbl_turno_top = tk.Label(janela, text = ("Escolha o turno:"))
# lbl_turno_top.grid (row=6, column=0, pady=10, padx=10)

# # ComboBox
# combo_nivel = tk.ttk.Combobox(janela, values=["A", "B", "C"], width=30)
# combo_nivel.grid(row=6, column=2, pady=10, padx=10)

# # Entrys
# usuario_nome = tk.Entry(janela, font=("Arial", 12))
# usuario_nome.grid(row=3,column=2,pady=10,padx=10)
# # Botão
# btn_enviar_mensagem = tk.Button(janela, text="Enviar Mensagem", bg="#a06bdd", fg="White" ,command=turno)
# btn_enviar_mensagem.grid(row=10, column=16, pady=145, padx=20)


# # Rodar interface
# janela.mainloop()




# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.


# import tkinter as tk
# from tkinter import messagebox,ttk

# # Criar Janela
# janela = tk.Tk()
# janela.title("Janela da Somativa")
# janela.geometry("800x400")
# #  Criar os componentes

# #def
# def calculo():
#     quant_d_p_em_1h = int(h1_em_p_d_quant.get())
    

#     if quant_d_p_em_1h == "" and p_8h =="":
#         messagebox.showwarning("Aviso", "Por favor digite a quantidade de peças feitas em 1 hora  :)")
#     else:
       
#          p_8h = quant_d_p_em_1h*8  
#          messagebox.showinfo("Bem-Vindo",f"Em 8 horas,terá sido produzindo {p_8h} " )


# #  Criar função do botão

# lbl_titulo = tk.Label(janela, text="Cálculo de Produção", font=("Arial",14,"bold"))
# lbl_titulo.grid(row=0, column=2, padx=10, pady=10)

# # Labels
# lbl_quant_d_p_em_1h = tk.Label(janela, text="Digite a quantidade de peças que são feitas em 1 hora:")
# lbl_quant_d_p_em_1h.grid(row=3, column=0, pady=10, padx=10)

# # ComboBox

# # Entrys
# h1_em_p_d_quant = tk.Entry(janela, font=("Arial", 12))
# h1_em_p_d_quant.grid(row=3,column=2,pady=10,padx=10)

# # Botão

# btn_enviar_mensagem = tk.Button(janela, text="Enviar Mensagem", bg="#a06bdd", fg="White" ,command=calculo)
# btn_enviar_mensagem.grid(row=10, column=16, pady=145, padx=20)

# # Rodar interface
# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.


# import tkinter as tk
# from tkinter import messagebox,ttk



# #  Criar os componentes

# #def
# def temperatura():
#     bar = float(bar_1.get())

#     if bar == "":
#         messagebox.showwarning("Aviso", "Digite a temperatura de Bar (; )")

#     else:
#         psi=bar*14.5
#         messagebox.showinfo("Bem-Vindo", f"A temperatura em PSI é {psi}")

# # Criar Janela
# janela = tk.Tk()
# janela.title("Janela da Somativa")
# janela.geometry("800x400")

# #  Criar função do botão
# lbl_titulo = tk.Label(janela, text="Transformação de Temperatura de Bar para PSI", font=("Arial",14,"bold"))
# lbl_titulo.grid(row=0, column=2, padx=10, pady=10)

# # Labels
# lbl_bar = tk.Label(janela,text="Digite a temperatura em Bar:")
# lbl_bar.grid(row=3,column=1,pady=10,padx=10)

# # ComboBox

# # Entrys
# bar_1 = tk.Entry(janela, font=("Arial", 12))
# bar_1.grid(row=3,column=2,pady=10,padx=10)
# # Botão
# btn_enviar_mensagem = tk.Button(janela, text="Enviar Mensagem", bg="#a06bdd", fg="White" ,command=temperatura)
# btn_enviar_mensagem.grid(row=10, column=16, pady=145, padx=20)

# # Rodar interface
# janela.mainloop()


# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox,ttk

# # Criar Janela
# janela = tk.Tk()
# janela.title("Janela da Somativa")
# janela.geometry("800x400")

# #  Criar os componentes

# #def
# def notas ():
#     combo_1= int(combo_1_entry.get())
#     combo_2= int(combo_2_entry.get())
#     combo_3= int(combo_3_entry.get())
    
#     if combo_1 == "" and combo_2 == "" and combo_3 == "":
#         messagebox.showwarning("Aviso","Selecione A nota de cada uma das peças (;)")
#     else:
#         cont = combo_1 + combo_2 + combo_3 / 3
    
#         messagebox.showinfo("Bem-Vindo",f"A média das notas dadas por você foi de {cont}")


   

# #  Criar função do botão

# # Labels
# lbl_combo1=tk.Label(janela,text="Digite a nota da peça 1:")
# lbl_combo1.grid(row=3,column=1,pady=10,padx=10)

# lbl_combo2=tk.Label(janela,text="Digite a nota da peça 2:")
# lbl_combo2.grid(row=4,column=2,pady=10,padx=10)


# lbl_combo3=tk.Label(janela,text="Digite a nota da peça 3:")
# lbl_combo3.grid(row=5,column=3,pady=10,padx=10)


# # ComboBox
# combo_1_entry = tk.ttk.Combobox(janela, values=["1","2","3","4","5","6","7","8","9","10"], width=30)
# combo_1_entry.grid(row=5, column=1, pady=10, padx=10)

# combo_2_entry = tk.ttk.Combobox(janela, values=["1","2","3","4","5","6","7","8","9","10"], width=30)
# combo_2_entry.grid(row=6, column=2, pady=10, padx=10)


# combo_3_entry = tk.ttk.Combobox(janela, values=["1","2","3","4","5","6","7","8","9","10"], width=30)
# combo_3_entry.grid(row=7, column=3, pady=10, padx=10)

# # Entrys

# # Botão
# btn_enviar_mensagem = tk.Button(janela, text="Enviar Mensagem", bg="#a06bdd", fg="White" ,command=notas)
# btn_enviar_mensagem.grid(row=10, column=16, pady=145, padx=20)

# # Rodar interface
# janela.mainloop()


# Foco: if, elif, else e operadores lógicos


# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

import tkinter as tk
from tkinter import messagebox,ttk

# Criar Janela
janela = tk.Tk()
janela.title("Janela da Somativa")
janela.geometry("800x400")

#  Criar os componentes

#def
def termostato ():
    temp = temperatu 
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
    if temp <= 40:
        messagebox.showwarning("Aviso","Baixa Carga")
    elif temp > 40 and temp < 70:
        messagebox.showinfo("Aviso"," Normal")




#  Criar função do botão
lbl_titulo = tk.Label(janela, text="Termostato Inteligente", font=("Arial",14,"bold"))
lbl_titulo.grid(row=0, column=2, padx=10, pady=10)

# Labels
lbl_temperatu=tk.Label(janela,text="Digite a temperatura:")
lbl_temperatu.grid(row=3,column=1,pady=10,padx=10)

# ComboBox

# Entrys

# Botão

# Rodar interface
janela.mainloop()








# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".


# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.


# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".


# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.