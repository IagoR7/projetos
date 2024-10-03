import customtkinter as ctk
from tkinter import messagebox

#-----\\--- Funções ---\\--------\\--------\\-----------\\-----------\\---------\\---

def calculo():
    doll = float(dol.get())
    calc = float(valordol.get())

    calcdoll = calc*doll
    #resultado.configure(text=f'O valor em Real é: R$ {calcdoll:.2f}')
    messagebox.showinfo('Valor final', f'O valor em Real é: R$ {calcdoll:.2f}')





#----\\----------\\--------\\------------\\-----------------\\---------------\\---






#------------------------ CAIXA -------------------------

ctk.set_appearance_mode('dark')
janela = ctk.CTk('gray')
janela.geometry('800x600')
janela.resizable(width=False,height=False)
janela.title('Sistema de Conversão')
janela.iconbitmap('Coin_icon-icons.com_67575.ico')

ctk.CTkLabel(janela,
             text='Sistema de Conversão V1.0',
             font=('verdana',40,'bold'),
             text_color='white').pack(pady=20)


#-------------- CAIXA DE ENTRADA QUANTIDADE DOLLAR -------
dol = ctk.CTkEntry(janela,
                   width=400,
                   height=40,
                   placeholder_text='Digite a quantia')
dol.pack(pady=15)
#----------------------------------------------------------

#------------ CAIXA DA COTAÇÃO DO DOLLAR -----------
valordol = ctk.CTkEntry(janela,
                   width=400,
                   height=40,
                   placeholder_text='Digite a cotação')
valordol.pack(pady=15)
#------------------------------------------------------

#-------------- BOTÃO ------------
botao = ctk.CTkButton(janela,
                      width=200,
                      height=30,
                      text='Converter',
                      cursor='hand2',
                      text_color='white',
                      command=calculo)
botao.pack(pady=10)
#----------------------------------------


#------------ EXIBIDOR DE RESULTADO ---------
resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('verdana',20,'bold'),
                         text_color='darkorange')
resultado.pack(pady=10)

#--------------------------------------------------------






janela.mainloop()

#------------------- FIM DA CAIXA ----------------------