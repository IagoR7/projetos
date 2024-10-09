import customtkinter as ctk

#-------Funções--------------

def button1():
    n1 = int(num1.get())
    n2 = int(num2.get())
    bt1 = n1+n2
    resultado.configure(text=f'O resultado é: {bt1}')

def button2():
    n1 = int(num1.get())
    n2 = int(num2.get())
    bt2 = n1-n2
    resultado.configure(text=f'O resultado é: {bt2}')

def button3():
    n1 = int(num1.get())
    n2 = int(num2.get())
    bt3 = n1*n2
    resultado.configure(text=f'O resultado é: {bt3}')

def button4():
    n1 = int(num1.get())
    n2 = int(num2.get())
    bt4 = n1/n2
    resultado.configure(text=f'O resultado é: {bt4}')









#-------------------------------

janela = ctk.CTk()
janela.geometry('800x600')
janela.title('Calculadora V1.0')
janela.resizable(width=False,height=False)
ctk.set_appearance_mode('dark')


ctk.CTkLabel(janela,
             text='Calculadora V1.0',
             font=('verdana',50,'bold')).pack(pady=20)


num1 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    placeholder_text='Digite o 1º número: ',
                    )
num1.pack(pady=10)

num2 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    placeholder_text='Digite o 2º número: ',
                    )
num2.pack(pady=10)

botao1 = ctk.CTkButton(janela,
                      width=400,
                      height=30,
                      text='+',
                      cursor='hand2',
                      command=button1)
botao1.pack(pady=10)
botao2 = ctk.CTkButton(janela,
                      width=400,
                      height=30,
                      text='-',
                      cursor='hand2',
                      command=button2)
botao2.pack(pady=10)
botao3 = ctk.CTkButton(janela,
                      width=400,
                      height=30,
                      text='',
                      cursor='hand2',
                      command=button3)
botao3.pack(pady=10)
botao4 = ctk.CTkButton(janela,
                      width=400,
                      height=30,
                      text='/',
                      cursor='hand2',
                      command=button4)
botao4.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('verdana',15,'bold'))
resultado.pack(pady=10)









janela.mainloop()