import customtkinter as cus
from tkinter import messagebox

#--------------Funções------------------

def viagem():
    d = int(distancia.get())
    c = int(consumo.get())
    g = float(precogaso.get())

    valor = (d/c)*g
    #resultado.configure(text = f'O valor total para a viagem sera de R$ {valor:.2f}' )
    messagebox.showinfo("Valor Final", f'O Valor da viagem sera R$ {valor:.2f}')







#-------------------------------------

cus.set_appearance_mode("dark")
janela = cus.CTk("black")
janela.geometry("800x800")
janela.resizable(width = False, height = False)
janela.title("APP VIAGEM")
#janela.iconbitmap("ic_vpn_lock_128_28770.ico")

cus.CTkLabel(janela,
             text="Sistema de Viagem - 1.0",
             font=("verdana", 45 , "bold"),
             text_color="yellow").pack(pady=20)

distancia = cus.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text="Digite a distancia para o destino",
                     corner_radius=60)

distancia.pack()

consumo = cus.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text="Digite o consumo",
                     corner_radius=60
                     )

consumo.pack(pady = 10)


precogaso = cus.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text="Digite o preço do combustivel",
                     corner_radius=60)

precogaso.pack()



botao = cus.CTkButton(janela,
                      width=150,
                      height=30,
                      fg_color="gray",
                      text='Calcular',
                      cursor="hand2",
                      text_color="black",
                      hover_color= 'orange',
                      corner_radius=60,
                      command= viagem)
                      

botao.pack(pady = 10)

resultado = cus.CTkLabel(janela,
             text=(),
             font=("verdana", 20 , "bold"),
             text_color="yellow")
resultado.pack(pady=10)
janela.mainloop()