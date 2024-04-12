from tkinter import *
import customtkinter as ct
from scipy.integrate import quad


def deprecicao(valor_inicial, porcentagem, vida_util, finalInterval):
    valor_residual = valor_inicial * porcentagem
    depreciacao_anual = (valor_inicial - valor_residual) / vida_util

    def equad(x):
        return depreciacao_anual * x / vida_util

    result, error = quad(equad, 0, finalInterval)

    return result


 
root = ct.CTk() 
root.title("Cálculadora Depreciação")

root.geometry("300x470")
root.resizable(False, False)

#Inicio Widgets
valor_inicial = StringVar()
porcentagem = StringVar()
vida_util = StringVar()
ano_final = StringVar()

label = ct.CTkLabel(root, text="Insira o valor inicial do produto:")
label.place(relx=0.05, rely=0.03)

entry1 = ct.CTkEntry(root, textvariable= valor_inicial, placeholder_text="50000")
entry1.place(relx=0.05, rely=0.10)


label = ct.CTkLabel(root, text="Insira a porcentagem de depreciação do produto:")
label.place(relx=0.05, rely=0.20)

entry2 = ct.CTkEntry(root, textvariable= porcentagem, placeholder_text="1")
entry2.place(relx=0.05, rely=0.27)

label = ct.CTkLabel(root, text="%")
label.place(relx=0.53, rely=0.27)


label = ct.CTkLabel(root, text="Insira a vida útil do produto (em anos):")
label.place(relx=0.05, rely=0.37)

entry3 = ct.CTkEntry(root, textvariable=vida_util, placeholder_text="8")
entry3.place(relx=0.05, rely=0.44)


label = ct.CTkLabel(root, text="Insira a quantidade de anos depreciados:")
label.place(relx=0.05, rely=0.54)

entry4 = ct.CTkEntry(root, textvariable=ano_final, placeholder_text="6")
entry4.place(relx=0.05, rely=0.61)

#Fim Widgets
def calcular_depreciacao():
    try:
        valor_inicial_depr = int(valor_inicial.get())
        porcentagem_depr = float(porcentagem.get())/100
        vida_util_depr = int(vida_util.get())
        ano_final_depr = int(ano_final.get())

        depreciado = deprecicao(valor_inicial_depr, porcentagem_depr, vida_util_depr, ano_final_depr)

        label = ct.CTkLabel(root, text= "Valor Depreciado: R$")
        label.place(relx=0.05, rely=0.72)

        label = ct.CTkLabel(root, text= depreciado)
        label.place(relx=0.46, rely=0.72)
    except ValueError:
        print("Campos Invalidos")


button = ct.CTkButton(master=root, text="Calcular Depreciação", command=calcular_depreciacao)
button.place(relx=0.25, rely=0.95, anchor='s')
button = ct.CTkButton(master=root, text="Exibir Gráficos", command=calcular_depreciacao)
button.place(relx=0.75, rely=0.95, anchor='s')

root.mainloop()