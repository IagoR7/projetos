import customtkinter as cus
from tkinter import messagebox

#--------------Funções------------------

def resultadof():
    u1 = float(uni1.get())
    u2 = float(uni2.get())
    u3 = float(uni3.get())

    unifinal = (u1 + u2 + u3) / 3 
    if unifinal >= 5:
        resultado_texto = "Você está aprovado"
        cor = 'green'
    else:
        resultado_texto = "Você está reprovado"
        cor = "red"
    
    resultado.configure(text=resultado_texto + f"\nMédia: {unifinal:.2f}",
                        text_color = cor)
    







#-------------------------------------

cus.set_appearance_mode("dark")
janela = cus.CTk("black")
janela.geometry("800x800")
janela.resizable(width = False, height = False)
janela.title("Sistema Escola 2024")
#janela.iconbitmap("ic_vpn_lock_128_28770.ico")

cus.CTkLabel(janela,
             text="Sistema de Escola - 1.0",
             font=("verdana", 45 , "bold"),
             text_color="white").pack(pady=20)

uni1 = cus.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text="Digite a sua nota da primeir unidade",
                     corner_radius=60)

uni1.pack()

uni2 = cus.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text="Digite a sua nota da segunda unidade",
                     corner_radius=60
                     )

uni2.pack(pady = 10)


uni3 = cus.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text="Digite a sua nota da terceira unidade",
                     corner_radius=60)

uni3.pack()



botao = cus.CTkButton(janela,
                      width=150,
                      height=30,
                      fg_color="gray",
                      text='Media',
                      cursor="hand2",
                      text_color="black",
                      hover_color= 'orange',
                      corner_radius=60,
                      command= resultadof)
                      

botao.pack(pady = 10)

resultado = cus.CTkLabel(janela,
             text=(),
             font=("verdana", 20 , "bold"),
             text_color="yellow")
resultado.pack(pady=10)
janela.mainloop()