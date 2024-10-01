import customtkinter as cus
from tkinter import messagebox
import os

#--------------Funções------------------
def logoff():
    os.system("shutdown -l")

def desligar():
    os.system("shutdown -s -t 0")

def reiniciar():
    os.system("shutdown -r -t 0")





#-------------------------------------

cus.set_appearance_mode("dark")
janela = cus.CTk("white")
janela.geometry("400x500")
janela.resizable(width = False, height = False)
janela.title("BOMBA PATCH")
#janela.iconbitmap("ic_vpn_lock_128_28770.ico")

cus.CTkLabel(janela,
             text="Bomba Patch",
             font=("verdana", 45 , "bold"),
             text_color="black").pack(pady=20)

des = cus.CTkButton(janela,
                      width=150,
                      height=50,
                      fg_color="red",
                      text='DESLIGAR',
                      cursor="hand2",
                      text_color="black",
                      hover_color= 'orange',
                      corner_radius=60,
                      command=desligar)
                      

des.pack(pady = 20)

rei = cus.CTkButton(janela,
                      width=150,
                      height=50,
                      fg_color="yellow",
                      text='REINICIAR',
                      cursor="hand2",
                      text_color="black",
                      hover_color= 'green',
                      corner_radius=60,
                      command=reiniciar)
                      

rei.pack(pady = 20)

bloquear = cus.CTkButton(janela,
                      width=150,
                      height=50,
                      fg_color="yellow",
                      text='SAIR',
                      cursor="hand2",
                      text_color="black",
                      hover_color= 'green',
                      corner_radius=60,
                      command=logoff)
                      

bloquear.pack(pady = 20)

janela.mainloop()