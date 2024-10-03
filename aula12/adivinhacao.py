import customtkinter as ctk
import random
#-----\\--- Funções ---\\--------\\--------\\-----------\\-----------\\---------\\---
secret = random.randint(1,10)
def adivinhar():
    
    valor = int(num.get())
    if valor > secret:
        resultado.configure(text=f'O número secreto é menor!')
    elif valor < secret:
        resultado.configure(text=f'O número secreto é maior!')
    else:
        resultado.configure(text=f'Você Acertou!')








#----\\----------\\--------\\------------\\-----------------\\---------------\\---






#------------------------ CAIXA -------------------------

ctk.set_appearance_mode('dark')
janela = ctk.CTk('gray')
janela.geometry('800x600')
janela.resizable(width=False,height=False)
janela.title('Jogo de Adivinhação')

ctk.CTkLabel(janela,
             text='Jogo de Adivinhação V1.0',
             font=('verdana',40,'bold'),
             text_color='white').pack(pady=20)


#-------------- CAIXA DE ENTRADA -------
num = ctk.CTkEntry(janela,
                   width=400,
                   height=40,
                   placeholder_text='Digite o número: ')
num.pack(pady=15)
#----------------------------------------------------------


#-------------- BOTÃO ------------
botao = ctk.CTkButton(janela,
                      width=200,
                      height=30,
                      text='Enviar',
                      cursor='pirate',
                      text_color='white',
                      command=adivinhar)
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
